#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

local_218 = np.zeros(256).astype(np.uint16)
local_218[0] = 0;
local_218[1] = 0xac;
local_218[2] = 0x13e;
local_218[3] = 0x1bc;
local_218[4] = 0x22c;
local_218[5] = 0x290;
local_218[6] = 0x2eb;
local_218[7] = 0x33e;
local_218[8] = 0x38b;
local_218[9] = 0x3d2;
local_218[10] = 0x415;
local_218[11] = 0x453;
local_218[12] = 0x48e;
local_218[13] = 0x4c6;
local_218[14] = 0x4fb;
local_218[15] = 0x52d;
local_218[16] = 0x55d;
local_218[17] = 0x58b;
local_218[18] = 0x5b7;
local_218[19] = 0x5e1;
local_218[20] = 0x60a;
local_218[21] = 0x631;
local_218[22] = 0x657;
local_218[23] = 0x67b;
local_218[24] = 0x69e;
local_218[25] = 0x6c0;
local_218[26] = 0x6e2;
local_218[27] = 0x702;
local_218[28] = 0x721;
local_218[29] = 0x73f;
local_218[30] = 0x75c;
local_218[31] = 0x779;
local_218[32] = 0x795;
local_218[33] = 0x7b0;
local_218[34] = 0x7cb;
local_218[35] = 0x7e5;
local_218[36] = 0x7fe;
local_218[37] = 0x817;
local_218[38] = 0x82f;
local_218[39] = 0x847;
local_218[40] = 0x85e;
local_218[41] = 0x875;
local_218[42] = 0x88b;
local_218[43] = 0x8a1;
local_218[44] = 0x8b7;
local_218[45] = 0x8cc;
local_218[46] = 0x8e0;
local_218[47] = 0x8f5;
local_218[48] = 0x909;
local_218[49] = 0x91c;
local_218[50] = 0x92f;
local_218[51] = 0x942;
local_218[52] = 0x955;
local_218[53] = 0x967;
local_218[54] = 0x979;
local_218[55] = 0x98b;
local_218[56] = 0x99c;
local_218[57] = 0x9ae;
local_218[58] = 0x9bf;
local_218[59] = 0x9cf;
local_218[60] = 0x9e0;
local_218[61] = 0x9f0;
local_218[62] = 0xa00;
local_218[63] = 0xa10;
local_218[64] = 0xa1f;
local_218[65] = 0xa2f;
local_218[66] = 0xa3e;
local_218[67] = 0xa4d;
local_218[68] = 0xa5c;
local_218[69] = 0xa6a;
local_218[70] = 0xa79;
local_218[71] = 0xa87;
local_218[72] = 0xa95;
local_218[73] = 0xaa3;
local_218[74] = 0xab0;
local_218[75] = 0xabe;
local_218[76] = 0xacb;
local_218[77] = 0xad9;
local_218[78] = 0xae6;
local_218[79] = 0xaf3;
local_218[80] = 0xb00;
local_218[81] = 0xb0c;
local_218[82] = 0xb19;
local_218[83] = 0xb25;
local_218[84] = 0xb31;
local_218[85] = 0xb3e;
local_218[86] = 0xb4a;
local_218[87] = 0xb56;
local_218[88] = 0xb61;
local_218[89] = 0xb6d;
local_218[90] = 0xb79;
local_218[91] = 0xb84;
local_218[92] = 0xb8f;
local_218[93] = 0xb9b;
local_218[94] = 0xba6;
local_218[95] = 0xbb1;
local_218[96] = 0xbbc;
local_218[97] = 0xbc6;
local_218[98] = 0xbd1;
local_218[99] = 0xbdc;
local_218[100] = 0xbe6;
local_218[101] = 0xbf1;
local_218[102] = 0xbfb;
local_218[103] = 0xc05;
local_218[104] = 0xc10;
local_218[105] = 0xc1a;
local_218[106] = 0xc24;
local_218[107] = 0xc2e;
local_218[108] = 0xc37;
local_218[109] = 0xc41;
local_218[110] = 0xc4b;
local_218[111] = 0xc54;
local_218[112] = 0xc5e;
local_218[113] = 0xc67;
local_218[114] = 0xc71;
local_218[115] = 0xc7a;
local_218[116] = 0xc83;
local_218[117] = 0xc8c;
local_218[118] = 0xc96;
local_218[119] = 0xc9f;
local_218[120] = 0xca8;
local_218[121] = 0xcb0;
local_218[122] = 0xcb9;
local_218[123] = 0xcc2;
local_218[124] = 0xccb;
local_218[125] = 0xcd3;
local_218[126] = 0xcdc;
local_218[127] = 0xce4;
local_218[128] = 0xced;
local_218[129] = 0xcf5;
local_218[130] = 0xcfe;
local_218[131] = 0xd06;
local_218[132] = 0xd0e;
local_218[133] = 0xd16;
local_218[134] = 0xd1e;
local_218[135] = 0xd27;
local_218[136] = 0xd2f;
local_218[137] = 0xd36;
local_218[138] = 0xd3e;
local_218[139] = 0xd46;
local_218[140] = 0xd4e;
local_218[141] = 0xd56;
local_218[142] = 0xd5e;
local_218[143] = 0xd65;
local_218[144] = 0xd6d;
local_218[145] = 0xd74;
local_218[146] = 0xd7c;
local_218[147] = 0xd83;
local_218[148] = 0xd8b;
local_218[149] = 0xd92;
local_218[150] = 0xd9a;
local_218[151] = 0xda1;
local_218[152] = 0xda8;
local_218[153] = 0xdaf;
local_218[154] = 0xdb6;
local_218[155] = 0xdbe;
local_218[156] = 0xdc5;
local_218[157] = 0xdcc;
local_218[158] = 0xdd3;
local_218[159] = 0xdda;
local_218[160] = 0xde1;
local_218[161] = 0xde7;
local_218[162] = 0xdee;
local_218[163] = 0xdf5;
local_218[164] = 0xdfc;
local_218[165] = 0xe03;
local_218[166] = 0xe09;
local_218[167] = 0xe10;
local_218[168] = 0xe17;
local_218[169] = 0xe1d;
local_218[170] = 0xe24;
local_218[171] = 0xe2a;
local_218[172] = 0xe31;
local_218[173] = 0xe37;
local_218[174] = 0xe3e;
local_218[175] = 0xe44;
local_218[176] = 0xe4a;
local_218[177] = 0xe51;
local_218[178] = 0xe57;
local_218[179] = 0xe5d;
local_218[180] = 0xe64;
local_218[181] = 0xe6a;
local_218[182] = 0xe70;
local_218[183] = 0xe76;
local_218[184] = 0xe7c;
local_218[185] = 0xe82;
local_218[186] = 0xe88;
local_218[187] = 0xe8e;
local_218[188] = 0xe94;
local_218[189] = 0xe9a;
local_218[190] = 0xea0;
local_218[191] = 0xea6;
local_218[192] = 0xeac;
local_218[193] = 0xeb2;
local_218[194] = 0xeb8;
local_218[195] = 0xebd;
local_218[196] = 0xec3;
local_218[197] = 0xec9;
local_218[198] = 0xecf;
local_218[199] = 0xed4;
local_218[200] = 0xeda;
local_218[201] = 0xee0;
local_218[202] = 0xee5;
local_218[203] = 0xeeb;
local_218[204] = 0xef0;
local_218[205] = 0xef6;
local_218[206] = 0xefb;
local_218[207] = 0xf01;
local_218[208] = 0xf06;
local_218[209] = 0xf0c;
local_218[210] = 0xf11;
local_218[211] = 0xf17;
local_218[212] = 0xf1c;
local_218[213] = 0xf21;
local_218[214] = 0xf27;
local_218[215] = 0xf2c;
local_218[216] = 0xf31;
local_218[217] = 0xf37;
local_218[218] = 0xf3c;
local_218[219] = 0xf41;
local_218[220] = 0xf46;
local_218[221] = 0xf4b;
local_218[222] = 0xf51;
local_218[223] = 0xf56;
local_218[224] = 0xf5b;
local_218[225] = 0xf60;
local_218[226] = 0xf65;
local_218[227] = 0xf6a;
local_218[228] = 0xf6f;
local_218[229] = 0xf74;
local_218[230] = 0xf79;
local_218[231] = 0xf7e;
local_218[232] = 0xf83;
local_218[233] = 0xf88;
local_218[234] = 0xf8d;
local_218[235] = 0xf92;
local_218[236] = 0xf97;
local_218[237] = 0xf9c;
local_218[238] = 4000;
local_218[239] = 0xfa5;
local_218[240] = 0xfaa;
local_218[241] = 0xfaf;
local_218[242] = 0xfb4;
local_218[243] = 0xfb8;
local_218[244] = 0xfbd;
local_218[245] = 0xfc2;
local_218[246] = 0xfc6;
local_218[247] = 0xfcb;
local_218[248] = 0xfd0;
local_218[249] = 0xfd4;
local_218[250] = 0xfd9;
local_218[251] = 0xfde;
local_218[252] = 0xfe2;
local_218[253] = 0xfe7;
local_218[254] = 0xfeb;
local_218[255] = 0xff0;

lut1 = local_218

pprint(lut1)
plt.plot(lut1)

lut2 = np.zeros(257).astype(np.uint16)
lut3 = np.zeros(0x1400).astype(np.uint16)
lut4 = np.zeros(0x2c00).astype(np.uint16)
#Really weird variable names and code structure courtesy of Ghidra decompilation of xphase software
uVar2 = 0
lut2_idx = 0
while(True):
    iVar7 = uVar2
    iVar5 = iVar7 * 0x10
    if(iVar5 < lut1[0]):
        lut2[lut2_idx] = 0
    elif(lut1[0xff] < iVar5):
        lut2[lut2_idx] = 0xff0
    else:
        uVar2 = 0
        uVar8 = 0
        while(uVar2 < 0x100):
            iVar9 = uVar8
            if((lut1[uVar2] <= iVar5) and (iVar5 <= lut1[uVar2+1])):
                break
            uVar2 += 1
            uVar8 += 1
            iVar9 = 0xff

        #When will this eever be true?  I'm guessing this LUT function was written generically to handle LUTs other than the one xphase is using, probably kanged from somewhere
        if(lut1[iVar9] == lut1[iVar9 + 1]):
            print("DERP!")
            lut2[lut2_idx] = iVar9 << 4
        else:
            #some form of interpolation?
            iVar3 = lut1[iVar9 + 1] + iVar7 * -0x10
            iVar5 -= lut1[iVar9]
            iVar1 = iVar5 + iVar3
            lut2[lut2_idx] = (((iVar3 * iVar9 + iVar5 * (iVar9 + 1)) * 0x10 + (iVar1 >> 1)) / iVar1)
    uVar2 = iVar7 + 1
    lut2_idx += 1
    if(iVar7 >= 0x100):
        lut3_idx = 0x400
        iVar9 = 0
        iVar10 = 0
        while(iVar9 + 1 < 0x1000):
            iVar9 = iVar10
            iVar10 = iVar9 + 1
            iVar5 = iVar9 >> 4
            iVar7 = iVar9 + iVar5 * -0x10
            lut3[lut3_idx] = (lut2[iVar5 + 1] * iVar7 + 8 + lut2[iVar5] * (0x10 - iVar7)) >> 4
            lut3_idx += 1
        lVar6 = 0x200
        lut3_idx = 0
        #this seems to be a really inefficient way to pad the hole with the lowest value of the second LUT in LUT2...  gotta split these up
        while(lVar6 != 0):
            lut3[lut3_idx] = lut3[0x400]
            lut3[lut3_idx + 1] = lut3[0x400]
            lVar6 -= 1
            lut3_idx += 2
        
        #lut4 is broken, but it isn't used for DNG anyway so probably just going to comment this out or if(0) it for reference
        lVar6 = 0x800
        lut4_idx = 0
        iVar5 = 0xe
        while(lVar6 != 0):
            lut4[lut4_idx] = (iVar5 - 7) >> 1 + lut3[0x13ff]
            lut4[lut4_idx + 1] = iVar5 >> 1 + lut3[0x13ff]
            lVar6 -= 1
            lut4_idx += 2
            iVar5 += 0xe
        lVar6 = 0xe00
        lut4_idx = 0x1000
        while(lVar6 != 0):
            lut4[lut4_idx] = lut4[0xfff]
            lut4[lut4_idx + 1] = lut4[0xfff]
            lVar6 -= 1
            lut4_idx += 2
        break


#Color matrix pulled from ghidra
color_matrix = np.zeros(9).astype(np.int16)
color_matrix[0] = 0x4502;
color_matrix[1] = 0xd8f;
color_matrix[2] = 0xafc;
color_matrix[3] = 0x1357;
color_matrix[4] = 0x39dd;
color_matrix[5] = 0x11dd;
color_matrix[6] = 0x989;
color_matrix[7] = 0xef8;
color_matrix[8] = 0x4519;
lut2_numpy = np.round(np.interp(np.arange(256)*16, lut1, np.arange(256)*16)).astype(np.uint16)
pprint(lut2)
pprint(lut2_numpy)

pprint(color_matrix)
red = 23
green = 23
blue = 23
dred = ((color_matrix[2] * red +
                color_matrix[1] * green +
            color_matrix[0] * blue + 0x200) >> 10) + -0x380;
dblue = ((color_matrix[3] * blue +
                color_matrix[5] * red +
                color_matrix[4] * green + 0x200) >> 10) + -0x380;
dgreen = ((color_matrix[6] * blue +
                color_matrix[8] * red +
                color_matrix[7] * green + 0x200) >> 10) + -0x380;
plt.figure()
plt.plot(lut2)
plt.plot(np.interp(np.arange(256)*16, lut1, np.arange(256)*16))
plt.figure()
plt.plot(lut3)
plt.figure()
plt.plot(lut4)
plt.show()