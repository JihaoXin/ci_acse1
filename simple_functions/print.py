import numpy as np

__all__ = ['myprint']


def myprint():
    a = np.array([1, 2, 3, 4])
    print(a[0])
    return a[0]
