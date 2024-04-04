#!/usr/bin/env python3

import os
import numpy as np
import tifffile as TIFF
import pyexiv2
from turbojpeg import TurboJPEG
import argparse
from xphase_data import XphaseTransforms

#fugly, find a better solution for generating RATIONAL/SRATIONAL
def cm_to_flatrational(input_array):
    retarray = np.ones(input_array.size*2, dtype=np.int32)
    retarray[0::2] = (input_array.flatten()*10000).astype(np.int32)
    retarray[1::2] = 10000
    return retarray


xt = XphaseTransforms()
jpeg = TurboJPEG()

#DNG color matrix as SRATIONAL, pulled from an PanoManager DNG
dng_color_matrix = np.array([2147483647, 1268696091, -1208266623, 2147483647, -180777967, 2147483647,
                             -826519231, 2147483647, 2147483647, 1937550026, 683803903, 2147483647,
                             -128558463, 2147483647, 411880927, 2147483647, 2147483647, 2046508879], dtype=np.int32)

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
    help='path to input file')

args = vars(ap.parse_args())
jpeg_file = args['input']

filebase = os.path.splitext(jpeg_file)[0]
dngname = filebase + '.dng'

with open(args['input'], 'rb') as jpgfile:
    #Swap BGR to RGB
    bgrdata = jpeg.decode(jpgfile.read())
    rgbdata = bgrdata.copy()
    rgbdata[:,:,0] = bgrdata[:,:,2]
    rgbdata[:,:,2] = bgrdata[:,:,0]

    # It seems like every lens except 00, 01, 23, 24 are flipped upside down by PanoManager
    (garbage, lensnum, shotnum) = filebase.split("_",3)
    if int(lensnum) not in [0, 1, 23, 24]:
        rgbdata = np.fliplr(np.flipud(rgbdata))

    #Colorspace and transfer function conversion
    rawdata = xt.jpeg_to_raw(rgbdata).astype(np.uint16)

    dng_extratags = []
    dng_extratags.append(('ColorMatrix1', '2i', 9, dng_color_matrix))
    dng_extratags.append(('CalibrationIlluminant1', 'H', 1, 23)) #is there an enum for this in tifffile???  23 = D50
    dng_extratags.append(('BlackLevel', 'H', 1, 0)) #BlackLevel - We subtracted black during processing, so it is 0
    dng_extratags.append(('WhiteLevel', 'I', 1, 65281)) #WhiteLevel
    dng_extratags.append(('DNGVersion', 'B', 4, [1,4,0,0])) #DNGVersion
    dng_extratags.append(('DNGBackwardVersion', 'B', 4, [1,4,0,0])) #DNGBackwardVersion
    dng_extratags.append(('AsShotNeutral', '2I', 3, np.array([1, 1, 1, 1, 1, 1], dtype=np.uint32))) #Xphase pre-applies a D50 white balance so AsShotNeutral is 1.0, 1.0, 1.0

    with TIFF.TiffWriter(dngname) as dng:
        dng.write(rawdata,
                photometric=34892, #tiffile does not have enums for LinearRaw, use numeric instead
                extratags=dng_extratags)
