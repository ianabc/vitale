import sys
try:
    import numpy as np
except ImportError:
    print("This version REQUIRES numpy")
    sys.exit(1)
#
# The "Vitale" property: The first two digits are divisible by 2, the
# first 3 digits are divisible by 4 and so on. 
#
# Numpy version: If numpy has 128bit uInts (or Ints) then this would
# work, with 64 bit ints, it starts failing in the teens
#
# http://www.blog.republicofmath.com/the-number-3608528850368400786036725/
#
# Start with the even two digit numbers less than 100
#

try:
    vitale_dtype = np.int128
except AttributeError:
    vitale_dtype = np.int64
    pass

def vitaleproperty(n):
    if n == 2:
        return np.arange(10, 99, 2, dtype=vitale_dtype)
    else:
        res = vitaleproperty(n - 1)
        res = 10 * res[:, np.newaxis] + np.arange(10)
        assert np.all(res > 0)
        return res[np.where(res % n == 0)]

if __name__ == "__main__":
    n = 2
    nvnums = []
    while True:
        try:
            vitale_n = vitaleproperty(n)
        except AssertionError:
            print("Overflow likely for n=%d, INCOMPLETE!!!" % n)
            break
            pass
        if (vitale_n.size != 0):
            nvnums.append(len(vitale_n))
            n = n + 1
        else:
            break

    try:
        import matplotlib.pyplot as plt
        plt.plot(nvnums, 'ro', markersize=5)
        plt.ylim([0, max(nvnums)  * 1.1])
        plt.xlim([0, n+3])
        plt.show()
    except ImportError:
        print(nvnums)

