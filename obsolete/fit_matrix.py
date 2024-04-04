#!/usr/bin/env python3

import numpy as np

derpmat = np.array([[1.2, -0.1, -0.05],
                    [-0.2, 1.3, 0.05],
                    [-0.3, 0.1, 0.9]])

foo = np.random.rand(80,3)

dta = np.matmul(foo, derpmat)

print(derpmat)
print(np.matmul(np.matmul(np.linalg.inv(np.matmul(foo.T,foo)), foo.T), dta))
print(np.linalg.inv(np.matmul(np.matmul(np.linalg.inv(np.matmul(dta.T,dta)), dta.T), foo)))

print(dta)
print(np.matmul(derpmat.T, foo.T).T)