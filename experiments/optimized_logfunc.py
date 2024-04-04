#!/usr/bin/env python

import jax.numpy as np
from jax import grad
import matplotlib.pyplot as plt
from pprint import pprint
from scipy.optimize import root


def linearize_logcode(x, a, b, c):
     return np.power(2,x*a-b)-c

# first derivative of linearize_logcode()
linearize_slope = grad(linearize_logcode)

def log2_logcode(x, a, b, c):
     return np.log2(linearize_logcode(x, a, b, c))

def log2_lin(x, a, b, c):
     return np.log2(x)

# second derivative of log2(linearize_logcode(x))
logslope2_code = grad(grad(log2_logcode))

logslope2_lin = grad(grad(log2_lin))

# second derivative of log2(x)


def code2lin(x, a, b, c, xt):
     return np.where(x < xt, x, linearize_logcode(x, a, b, c))

def lin2code(x, a, b, c, xt):
     return np.where(x < xt, x, (np.log2(x+c)+b)/a)

def equations(vars):
     a, b, c, xt = vars
     eq1 = linearize_logcode(255, a, b, c) - 1023
     eq2 = linearize_slope(xt, a, b, c) - 1
     eq3 = linearize_logcode(xt, a, b, c) - xt
     eq4 = logslope2_code(xt, a, b, c) - logslope2_lin(xt, a, b, c)
     return [eq1, eq2, eq3, eq4]

initial_guess = np.array([ 0.01405711, -6.53891292, 92.50032936, 10.31508481])
solution = root(equations, initial_guess)
np.set_printoptions(suppress=True)
pprint(solution.x)

def equations2(vars):
     a, b, c, xt = vars
     eq1 = linearize_logcode(255, a, b, c) - 1023
     eq2 = linearize_slope(xt, a, b, c) - 1
     eq3 = linearize_logcode(xt, a, b, c) - xt
     eq4 = c
     return [eq1, eq2, eq3, eq4]

initial_guess = np.array([ 0.02091433, -4.66543526,  0.        , 68.98115442])
solution2 = root(equations2, initial_guess)
pprint(solution2.x)

a, b, c, xt = solution.x
a2, b2, c2, xt2 = solution2.x

print(linearize_slope(xt, a, b, c))

print(logslope2_code(xt, a, b, c))
print(logslope2_lin(xt, a, b, c))

codes = np.arange(255)
plt.plot(code2lin(codes, a, b, c, xt))
plt.plot(code2lin(codes, a2, b2, c2, xt2))

plt.figure()
lins = np.arange(1023)
plt.plot(lin2code(lins, a, b, c, xt))
plt.plot(lin2code(lins, a2, b2, c2, xt2))

plt.figure()
plt.plot(codes[:-1]+1, 1.0/np.diff(np.log2(code2lin(codes, a, b, c, xt))))
plt.plot(codes[:-1]+1, 1.0/np.diff(np.log2(code2lin(codes, a2, b2, c2, xt2))))

plt.figure()
plt.plot(np.log2(code2lin(codes[:-1]+1,a, b, c, xt)/1023), 1.0/np.diff(np.log2(code2lin(codes, a, b, c, xt))))
plt.plot(np.log2(code2lin(codes[:-1]+1,a2, b2, c2, xt2)/1023), 1.0/np.diff(np.log2(code2lin(codes, a2, b2, c2, xt2))))
plt.plot(np.log2((lins[:-1]+1)/1023), 1.0/np.diff(np.log2(lins/1023)))
plt.axhline(y=1.0/np.log2(1.02), color='k', alpha=0.5)
plt.axhline(y=1.0/np.log2(1.05), color='k', alpha=0.5)

plt.show()