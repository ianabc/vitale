#!/usr/bin/env python
#
# The "Vitale" property: The first two digits are divisible by 2, the
# first 3 digits are divisible by 4 and so on.
#
# http://www.blog.republicofmath.com/the-number-3608528850368400786036725/
#
# This program will calculate the vitale numbers. It uses python's
# arbitrary precision integer libraries.

def vitaleproperty(n):
    if n == 2:
        return range(10, 99, 2)
    else:
        vnums = []
        for vnum in vitaleproperty(n-1):
            vnum = vnum * 10
            for j in range(10):
                if ((vnum + j) % n == 0):
                    vnums.append(vnum + j)

        return vnums

if __name__ == "__main__":
    n = 2
    nvnums = []
    while True:
        vitale_n = vitaleproperty(n)
        if (len(vitale_n) > 0):
            nvnums.append(len(vitale_n))
            n = n + 1
        else:
            break

    try:
        import matplotlib.pyplot as plt
        plt.plot(nvnums, 'ro', markersize=5)
        plt.ylim([0, max(nvnums) * 1.1])
        plt.show()
    except ImportError:
        print (nvnums)

