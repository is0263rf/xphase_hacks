A few scripts for fiddling with the Xphase Pro camera family for those who already own one.

In addition to a bunch of analysis tools intended for fuzzing PanoManager which most users will never need (now located in the obsolete/ folder), and some proof-of-concept analysis of alternative luminance transfer curves (experiments/ folder), this repository now has the following tools that are of general use to normal users:

- unpackori.py - Unpacks an ORI file.
    - In its default mode, it unpacks all raw header and lens metadata blocks, along with raw JPEG images.  This is intended for use with packori.py
    - If passed the -d option, it will not write most of the raw header binaries, but will output colorspace-converted DNGs
    - If passed the -t option, it will not write most of the raw header binaries, but will output colorspace-converted TIFF files that have an appropriate ICC profile that matches the Xphase "raw" colorspace


- packori.py - Repacks an ORI file.  This can be used, for example, to allow images from two different shots to be mix-and-matched in a manner that offers more flexibility than the "half and half" mode added by Xphase in a firmware revision.  Options passed on the command line must match the kind of ORI being repacked (3 or 6 shot, Scan vs "not Scan")

- cnv_jpeg_to_dng.py - Converts a JPEG in Xphase's highly nonstandard colorspace to a DNG with appropriate color metadata.  Most of the time you are better off with the -d option to unpackori
- cnv_jpeg_to_tif.py - Converts a JPEG in Xphase's highly nonstandard colorspace to a TIFF with appropriate color metadata.  Most of the time you are better off with the -t option to unpackori

Call any of these scripts with the -h option to get usage information

The camera does now have a raw DNG option, although white balance is prescaled and the values are multiplied by 64 after white balance prescaling to fill an int16 with huge histogram gaps, making files 60% larger than not scaling anything and saving bitpacked data with BitsPerSample = 10.  The camera is known to tend to overheat when shooting these DNGs

Metadata support has been partially reverse engineered thanks to the NSA's Ghidra SRE tool, along with decompilation of a GPL-violating derivative of this work.  DNG and TIFF output will have metadata applied.  JPEG output will not, as this will interfere with packori and directly unpacked JPEGs are useless on their own due to Xphase's highly nonstandard and poorly designed color pipeline.
