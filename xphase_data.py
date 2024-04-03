#!/usr/bin/env python

import numpy as np

class XphaseTransforms:
    def __init__(self):

        # Pulled from PanoManager's PanoMakerPro.dll using Ghidra
        # This is in theory a close match to the camera's internal sensor->JPEG LUT, except only has
        # 256 entries for a 10 bit sensor...  Hisilicon limitation???
        self.lut = np.array([   0,  172,  318,  444,  556,  656,  747,  830,  907,  978, 1045,
       1107, 1166, 1222, 1275, 1325, 1373, 1419, 1463, 1505, 1546, 1585,
       1623, 1659, 1694, 1728, 1762, 1794, 1825, 1855, 1884, 1913, 1941,
       1968, 1995, 2021, 2046, 2071, 2095, 2119, 2142, 2165, 2187, 2209,
       2231, 2252, 2272, 2293, 2313, 2332, 2351, 2370, 2389, 2407, 2425,
       2443, 2460, 2478, 2495, 2511, 2528, 2544, 2560, 2576, 2591, 2607,
       2622, 2637, 2652, 2666, 2681, 2695, 2709, 2723, 2736, 2750, 2763,
       2777, 2790, 2803, 2816, 2828, 2841, 2853, 2865, 2878, 2890, 2902,
       2913, 2925, 2937, 2948, 2959, 2971, 2982, 2993, 3004, 3014, 3025,
       3036, 3046, 3057, 3067, 3077, 3088, 3098, 3108, 3118, 3127, 3137,
       3147, 3156, 3166, 3175, 3185, 3194, 3203, 3212, 3222, 3231, 3240,
       3248, 3257, 3266, 3275, 3283, 3292, 3300, 3309, 3317, 3326, 3334,
       3342, 3350, 3358, 3367, 3375, 3382, 3390, 3398, 3406, 3414, 3422,
       3429, 3437, 3444, 3452, 3459, 3467, 3474, 3482, 3489, 3496, 3503,
       3510, 3518, 3525, 3532, 3539, 3546, 3553, 3559, 3566, 3573, 3580,
       3587, 3593, 3600, 3607, 3613, 3620, 3626, 3633, 3639, 3646, 3652,
       3658, 3665, 3671, 3677, 3684, 3690, 3696, 3702, 3708, 3714, 3720,
       3726, 3732, 3738, 3744, 3750, 3756, 3762, 3768, 3773, 3779, 3785,
       3791, 3796, 3802, 3808, 3813, 3819, 3824, 3830, 3835, 3841, 3846,
       3852, 3857, 3863, 3868, 3873, 3879, 3884, 3889, 3895, 3900, 3905,
       3910, 3915, 3921, 3926, 3931, 3936, 3941, 3946, 3951, 3956, 3961,
       3966, 3971, 3976, 3981, 3986, 3991, 3996, 4000, 4005, 4010, 4015,
       4020, 4024, 4029, 4034, 4038, 4043, 4048, 4052, 4057, 4062, 4066,
       4071, 4075, 4080], dtype=np.uint16)

        # Rather than store the JPEG-to-RAW LUT directly, PanoManager interpolates from the above LUT
        # Experimentation verified that this provides identical results to PanoManager's LUT without
        # the padded 0xff0 in entry 257 which will never be used.  Xphase loves off-by-one errors in
        # their software...
        self.ilut = np.round(np.interp(np.arange(256)*16, self.lut, np.arange(256)*16)).astype(np.int32)
        
        # Also pulled from PanoMakerPro.dll using Ghidra
        self.jpeg_to_raw_matrix = np.array([17666,  3471,  2812,  4951, 14813,  4573,  2441,  3832, 17689], dtype=np.int16).reshape((3,3))


    def jpeg_to_raw(self, imagedata):
        # Invert Xphase's poorly designed JPEG pipeline
        # After applying a fixed D50 white balance to the raw sensor data (even out-of-camera DNGs have this...), the camera adds a black level offset for unknown reasons -
        # the only possible explanation is to desaturate darks to allow representing a wider gamut in the shadows but HDR merging will throw out the shadows of eveery JPEG,
        # except the darkest - so the gamut won't be expanded at any usable luminance, and this approach reduces usable luminance range.
        #
        # It then compresses 10 bits down to 8 using a variation of the LUT stored at the beginning of this file.  Afterwards, it encodes a YUV420 JPEG
        # using the standard JPEG RGB->YUV conversion matrix.
        #
        # The below inverse LUT followed by a matrix transformation then subtraction undoes this pipeline, and exactly matches PanoManager's conversion pipeline
        # Note the + 0x200 offset - this appears to be designed to convert a floor/truncation to rounding by adding a value that corresponds to 0.5 in floating point
        #, as 0x400 translates to 1 when right shifted by 10 bits.
        h = imagedata.shape[0]
        w = imagedata.shape[1]
        imagedata = imagedata.reshape((w*h, 3))
        rawdata = ((np.matmul(self.jpeg_to_raw_matrix, self.ilut[imagedata.T]).T + 0x200) >> 10) - 0x380
        rawdata = rawdata.reshape((h, w, 3))
        rawdata = np.clip(rawdata, 0, 0xff00).astype(np.uint16)
        # Xphase adds 1 to everything on export.  WHY?  This will cause a black level offset in the shadows
        # FIXME:  Make this behavior an option
        return rawdata + 1
