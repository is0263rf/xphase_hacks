#!/usr/bin/env python3

import sys
import os
import colour
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from xphase_data import XphaseTransforms

xt = XphaseTransforms()

rgbdata_1ev = np.array([[182, 0, 0],
                        [0, 182, 0],
                        [0 ,0, 182]]).astype(np.uint8)

rgbdata_2ev = np.array([[142, 0, 0],
                        [0, 142, 0],
                        [0, 0, 142]]).astype(np.uint8)

rgbdata_1ev = rgbdata_1ev.reshape((rgbdata_1ev.shape[0],1,3))

rgbdata_2ev = rgbdata_2ev.reshape((rgbdata_2ev.shape[0],1,3))

#DNG color matrix
color_matrix_dng = np.matrix([[1.69266987, -0.5626429913, -0.08418130087],
                              [-0.3848780093, 1.108350039, 0.3184210059],
                              [-0.0598646994, 0.1917970028, 1.04934001]])
invmatrix_dng = np.linalg.inv(color_matrix_dng)
primaries_dng = colour.primaries_whitepoint(invmatrix_dng)[0]
whitepoint_dng = colour.primaries_whitepoint(invmatrix_dng)[1]
colorspace_dng = colour.models.RGB_Colourspace('RAW color space', primaries_dng, whitepoint_dng, use_derived_matrix_RGB_to_XYZ=True, use_derived_matrix_XYZ_to_RGB=True)

rawdata_1ev = xt.jpeg_to_raw(rgbdata_1ev)
xyzprim_1ev = colour.RGB_to_XYZ(rawdata_1ev, colourspace=colorspace_dng)
xyprim_1ev = colour.XYZ_to_xy(xyzprim_1ev)

rawdata_2ev = xt.jpeg_to_raw(rgbdata_2ev)
xyzprim_2ev = colour.RGB_to_XYZ(rawdata_2ev, colourspace=colorspace_dng)
xyprim_2ev = colour.XYZ_to_xy(xyzprim_2ev)

colorspace_1ev = colour.models.RGB_Colourspace('-1EV gamut', xyprim_1ev, whitepoint_dng, use_derived_matrix_RGB_to_XYZ=True, use_derived_matrix_XYZ_to_RGB=True)

colorspace_2ev = colour.models.RGB_Colourspace('-2EV gamut', xyprim_2ev, whitepoint_dng, use_derived_matrix_RGB_to_XYZ=True, use_derived_matrix_XYZ_to_RGB=True)

colour.plotting.plot_RGB_colourspaces_in_chromaticity_diagram_CIE1931([colorspace_dng, colorspace_1ev, colorspace_2ev, colour.models.RGB_COLOURSPACE_sRGB])