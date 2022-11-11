#!/usr/bin/env python3

import cv2
from turbojpeg import TurboJPEG, TJSAMP_420
import sys
import numpy as np
import matplotlib.pyplot as plt

jpeg = TurboJPEG()

w = 3264
h = 2448

uw = w//2
uh = h//2
hald_level = 11

for y in np.floor(np.linspace(0,255,9)).astype(np.uint8):
    ydata = np.ones((h,w),dtype=np.uint8)*y
    udata = np.ones((uh, uw), dtype=np.uint8)
    vdata = np.ones((uh, uw), dtype=np.uint8)

    udata *= np.floor(np.linspace(0, 255, uw)).astype(np.uint8)
    vdata *= np.floor(np.linspace(0, 255, uh)).astype(np.uint8)[:,np.newaxis]


    imgdata = np.concatenate((np.reshape(ydata,w*h),np.reshape(udata,uw*uh),np.reshape(vdata,uw*uh)), dtype=np.uint8)

    with open('mutlihue_' + str(y) + '.jpg', 'wb') as outfile:
        outfile.write(jpeg.encode_from_yuv(imgdata, h, w, quality=99, jpeg_subsample=TJSAMP_420))

for y in np.floor(np.linspace(0,255,9)).astype(np.uint8):
    ydata = np.ones((h,w),dtype=np.uint8)*y
    udata = np.ones((uh, uw), dtype=np.uint8)
    vdata = np.ones((uh, uw), dtype=np.uint8)*128

    udata *= np.floor(np.linspace(0, 255, uw)).astype(np.uint8)

    imgdata = np.concatenate((np.reshape(ydata,w*h),np.reshape(udata,uw*uh),np.reshape(vdata,uw*uh)), dtype=np.uint8)

    with open('ugradient_' + str(y) + '.jpg', 'wb') as outfile:
        outfile.write(jpeg.encode_from_yuv(imgdata, h, w, quality=99, jpeg_subsample=TJSAMP_420))

for y in np.floor(np.linspace(0,255,9)).astype(np.uint8):
    ydata = np.ones((h,w),dtype=np.uint8)*y
    udata = np.ones((uh, uw), dtype=np.uint8)*128
    vdata = np.ones((uh, uw), dtype=np.uint8)

    vdata *= np.floor(np.linspace(0, 255, uw)).astype(np.uint8)

    imgdata = np.concatenate((np.reshape(ydata,w*h),np.reshape(udata,uw*uh),np.reshape(vdata,uw*uh)), dtype=np.uint8)

    with open('vgradient_' + str(y) + '.jpg', 'wb') as outfile:
        outfile.write(jpeg.encode_from_yuv(imgdata, h, w, quality=99, jpeg_subsample=TJSAMP_420))

udata = np.ones((uh, uw), dtype=np.uint8)*128
vdata = np.ones((uh, uw), dtype=np.uint8)*128
ydata = (np.ones((h,w)) * np.floor(np.linspace(0,255, w))).astype(np.uint8)

imgdata = np.concatenate((np.reshape(ydata,w*h),np.reshape(udata,uw*uh),np.reshape(vdata,uw*uh)), dtype=np.uint8)

with open('grayband.jpg', 'wb') as outfile:
    outfile.write(jpeg.encode_from_yuv(imgdata, h, w, quality=99, jpeg_subsample=TJSAMP_420))