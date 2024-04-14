#!/usr/bin/env python3

import os
import sys
import platform
import numpy as np
import tifffile
import imagecodecs
import pyexiv2
from turbojpeg import TurboJPEG, TJPF_RGB
import argparse
from xphase_data import XphaseTransforms

def write_tiff(jpegdata, exifdata, filebase):
    dll_names = {'Windows' : 'libturbojpeg.dll',
                'Linux' : 'libturbojpeg.so'}
    def init_TurboJPEG():
        if(hasattr(sys, 'frozen')):
            #Running under PyInstaller
            if(getattr(sys, 'frozen') == True):
                dll_path = os.path.join(getattr(sys, '_MEIPASS'), 'turbojpeg.libs', dll_names[platform.system()])
                return TurboJPEG(dll_path)
            else:
                exit('Running under PyInstaller single-file mode not yet supported')
        else:
            return TurboJPEG()

    xt = XphaseTransforms()
    jpeg = init_TurboJPEG()


    #Raw primaries and whitepoint derived from Xphase's ColorMatrix1 in xyY coordinates
    raw_primaries = np.array([[ 0.74492141,  0.26012652,  0.23330306],
        [ 0.27952073,  0.86210755,  1.07382486],
        [-0.08045753, -0.47473468, -0.30713461]])
    raw_whitepoint = np.array([ 0.34566994,  0.35849447,  0.99999331])

    #ICC profile that corresponds to Xphase's raw colorspace
    icc_profile = imagecodecs.cms_profile('rgb', whitepoint=raw_whitepoint, primaries=raw_primaries.reshape(9), gamma=1.0)

    tifname = filebase + '.tif'

    rgbdata = jpeg.decode(jpegdata, pixel_format=TJPF_RGB)

    # It seems like every lens except 00, 01, 23, 24 are flipped upside down by PanoManager
    (garbage, lensnum, shotnum) = filebase.split("_",3)
    if int(lensnum) not in [0, 1, 23, 24] and exifdata['Exif.Image.Model'] != 'Scan':
        rgbdata = np.fliplr(np.flipud(rgbdata))

    #Colorspace and transfer function conversion
    rawdata = xt.jpeg_to_raw(rgbdata).astype(np.uint16)

    with tifffile.TiffWriter(tifname) as tif:
        tif.write(rawdata,
                photometric='rgb',
                compression='zlib',
                predictor=True,
                extratags=[('InterColorProfile', tifffile.DATATYPE.BYTE, len(icc_profile), icc_profile)])

    with pyexiv2.Image(tifname) as tif:
        tif.modify_exif(exifdata)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True,
        help='path to input file')

    args = vars(ap.parse_args())
    jpeg_file = args['input']

    filebase = os.path.splitext(jpeg_file)[0]

    xphase_exif = {'Exif.Image.Make': 'Xphase',
                'Exif.Image.Model': 'Xphase'}

    with open(jpeg_file, 'rb') as jpgfile:
        write_tiff(jpgfile.read(), xphase_exif, filebase)