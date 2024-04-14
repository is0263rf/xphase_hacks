#!/usr/bin/python3

#Copyright 2019 Andrew T. Dodd

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#horribly hackish Xphase ORI unpacker
#much code kanged from stackoverflow samples -
# https://stackoverflow.com/questions/49182097/searching-for-all-occurance-of-byte-strings-in-binary-file
# https://stackoverflow.com/questions/2363483/python-slicing-a-very-large-binary-file

import os
import argparse
import struct
from cnv_jpeg_to_dng import write_dng
from cnv_jpeg_to_tiff import write_tiff

def copypart(src,dest,start,length,bufsize=1024*1024):
    with open(src,'rb') as f1:
        f1.seek(start)
        with open(dest,'wb') as f2:
            while length:
                chunk = min(bufsize,length)
                data = f1.read(chunk)
                f2.write(data)
                length -= chunk

def parse_header(headerdata, shotnum):
    xphase_exif = {'Exif.Image.Make': 'Xphase',
                'Exif.Image.Model': 'Xphase'}
    return xphase_exif

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
    help='path to input file')

ap.add_argument('--dateheader', action='store_true')
ap.add_argument('-d', '--dng', action='store_true')
ap.add_argument('-t', '--tiff', action='store_true')
ap.add_argument('-p', '--save_preview', action='store_true')

args = vars(ap.parse_args())
bin_file = args['input']

(filebase, ext) = bin_file.rsplit('.',1)

conversion_mode = args['dng'] or args['tiff']

with open(bin_file,'rb') as myfile:
    cur_offset = 2

    blocknum = 0
    myfile.seek(0, os.SEEK_END)
    filelen = myfile.tell()

    while(cur_offset < filelen):
        myfile.seek(cur_offset)
        (blocktype, nbytes) = struct.unpack('<hL', myfile.read(6))
        if not conversion_mode:
            print("Block number " + str(blocknum) + " has type " + str(blocktype) +
                " with length " + str(nbytes) + " at offset " + hex(cur_offset + 6))

        if(blocktype == -48):
            myfile.seek(cur_offset + 6)
            headerdata = myfile.read(nbytes)
            if not conversion_mode:
                print("\tFile header data")
                if(args['dateheader']):
                    hfilename = 'headerdata_'+filebase+'.bin'
                else:
                    hfilename = 'headerdata.bin'
                with open(hfilename, 'wb') as headerfile:
                    headerfile.write(headerdata)

            # Everything appears to be stored as signed or maybe unsigned int32
            # Date is year, month, day, hour, minute, second starting at offset 8
            # 0x38 appears to be proportional to exposure time, but has different meaning whether HDR3 or HDR6
            # shuttertime * 7680 for HDR6
            # shuttertime * 30840 for HDR3
            # 0x44 is ISO/6.25
            # Offset 0x68 = EV offset divided by 3
            # 0x70 = 2 for HDR3, 4 for HDR6, but not the only thing that is used to differentiate.  Repacking as 3-shot without changing this will cause PM to ignore the file
            #   but changing this and repacking will cause PM to recognize the file, but still display as HDR6 and fail to stitch

            # Offsets from Ghidra decompilation of PanoManager's header parser function.  These are int offsets, multiply by 4 to get byte offsets
            # 0 = model.  2 = S, 3 = S2, 4 = X2, anything else is currently Scan.  FIXME:  Find model ID from a Scan ORI
            # 0x1c = HDR mode.  Value less than 4 is HDR3, value less than 6 (5 by process of elimination) is HDR6, otherwise HDR6+
            # LSB appears to be AE mode.  0 = Manual, 1 = Auto
            # 0x3a = Shot count? if nonzero.  If zero, shot count appears to depend on HDR mode: 1 for mode < 4 (HDR3), 3 otherwise.  Maybe lens index for displayed metadata since this appears to be middle shot?
            # Xphase carefully clamps this to a value between 0 and 5 inclusive
            # and shot count of 0 for HDR3 is old firmware behavior
            # Bunch of shot-specific data in two groups:
            # iVar15 = 0xa + shotnum*4 for shotnum < 3, 0x2e + (shotnum-3)*4 else
            # iVar10 = add 2 to all offsets for iVar15
            # iVar5 = add 1 to all iVar10 offsets
            # 1 is an unused offset in the function I'm looking at
            # Later on in parser:
            #   local_3c8 = (longlong **)
            #  CONCAT44(local_3c8._4_4_,(int)(iVar5 * 100 + (iVar5 * 100 >> 0x1f & 0xfU)) >> 4); - ISO???
            # also
            #  dVar16 = (double)(iVar10 * iVar15) / 120000000.0; - exposure time?  Since 0xe int offset = 0x38 byte offset
            # Some string is "NO" unless 0x2c and 0x2d are nonzero, it becomes "OK" then - looks like GPS, probably lat and long

        elif(blocktype == -40):
            if not conversion_mode:
                myfile.seek(cur_offset + 6)
                print("\tSmall lens data blocks (32 bytes per lens)")
                with open('smallblock.bin', 'wb') as smallblockfile:
                    smallblockfile.write(myfile.read(nbytes))

        elif(blocktype == -41):
            if not conversion_mode:
                myfile.seek(cur_offset + 6)
                print("\tLarge lens data blocks (3080 bytes per lens)")
                with open('largeblock.bin', 'wb') as largeblockfile:
                    largeblockfile.write(myfile.read(nbytes))

        elif(blocktype == -39):
            tablestart = cur_offset + 6
            tablelen = nbytes
            myfile.seek(tablestart)
            oritable = myfile.read(tablelen)
            if not conversion_mode:
                with open('oritable.bin', 'wb' ) as tablefile:
                    tablefile.write(oritable)
                print("\tORI image table found")

        elif(blocktype == -45):
            imgstart = cur_offset + 6
            if not conversion_mode:
                print("\tImage data block found")

        elif(blocktype == -46):
            if not conversion_mode:
                previewstart = cur_offset + 6
                myfile.seek(previewstart)
                print("\tSpare duplicate image block found")
                with open('sparedup.jpg', 'wb') as sparedupfile:
                    sparedupfile.write(myfile.read(nbytes))

        elif(blocktype == -43):
            if not conversion_mode:
                previewstart = cur_offset + 6
                print("\tUser Nadir image block found")
                myfile.seek(previewstart)
                with open('usernadir.jpg', 'wb') as previewfile:
                    previewfile.write(myfile.read(nbytes))

        else:
            print("\tUnknown block type" + str(blocktype))
        cur_offset += 6 + nbytes

    for entrynum in range(int(tablelen/20)):
        tbloffset = entrynum * 20
        (imgtype, lens, shot, fileoffset, filelen) = struct.unpack_from('<HHHxxxxxxLL', oritable, offset=tbloffset)
        filestart = imgstart + fileoffset
        if(filelen > 0):
            if(imgtype == 1):
                if args['save_preview']:
                    dest_fname = "IMG_" + format(lens, '#02') + "_" + str(shot) + "_preview.jpg"
                    copypart(bin_file, dest_fname, filestart, filelen)
            elif(imgtype == 2):
                dest_basename = "IMG_" + format(lens, '#02') + "_" + str(shot)
                exifdata = parse_header(headerdata, shot)
                if args['tiff']:
                    myfile.seek(filestart)
                    write_tiff(myfile.read(filelen), exifdata, dest_basename)
                if args['dng']:
                    myfile.seek(filestart)
                    write_dng(myfile.read(filelen), exifdata, dest_basename)
                if not conversion_mode:
                    copypart(bin_file, dest_basename + ".jpg", filestart, filelen)
            else:
                print("Unknown image type " + str(imgtype) + " found in ORI table in entry " + str(entrynum) + ", aborting")
                exit(-1)


