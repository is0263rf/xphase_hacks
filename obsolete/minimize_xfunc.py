#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from xphase_data import XphaseTransfer

lut = XphaseTransfer().lut

codes = (np.arange(230-23)+23)

def linearize_code(x, a, b, c):
     return np.power(2,(x*a-b))-c

def log2_code(x, a, b, c):
     return np.log2(linearize_code(x, a, b, c))

def linearize_code2(x, a, b, c, xt):
     s = np.log(2)*a*np.power(2, xt*a - b)
     return np.where(x < xt, s*(x-xt) + linearize_code(xt, a, b, c), linearize_code(x, a, b, c))

def log2_code2(x, a, b, c, xt):
     return np.log2(linearize_code2(x, a, b, c, xt))

popt, _ = curve_fit(log2_code, codes, np.log2(lut[codes]))
popt2, _ = curve_fit(linearize_code, codes, lut[codes])

print(popt)
print(popt2)
a, b, c = popt

popt3, _ = curve_fit(log2_code2, codes, np.log2(lut[codes]), p0=[a, b, c, 30])
popt4 , _ = curve_fit(linearize_code2, codes, lut[codes], p0=[a, b, c, 30])

print(popt3)
print(popt4)
a, b, c, xt = popt3

plt.plot(np.arange(255),lut[np.arange(255)])
plt.plot(np.arange(255),linearize_code(np.arange(255),a,b,c))

plt.figure()
plt.plot(np.arange(254)+1,np.diff(lut[np.arange(255)]))
plt.plot(np.arange(254)+1,np.diff(linearize_code(np.arange(255),a,b,c)))

plt.figure()
plt.plot(np.arange(255),np.log2(lut[np.arange(255)]))
plt.plot(np.arange(255),log2_code(np.arange(255), a, b, c))

plt.figure()
plt.plot(np.arange(254)+1,1.0/np.diff(np.log2(lut[np.arange(255)])))
plt.plot(np.arange(254)+1,1.0/np.diff(log2_code(np.arange(255), a, b, c)))
plt.axhline(1.0/np.log2(1.05), color='k', alpha=0.5)
plt.axhline(1.0/np.log2(1.02), color='k', alpha=0.5)
plt.show()