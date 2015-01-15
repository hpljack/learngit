__author__ = 'Administrator'

from math import pi,fsum


if __name__ == '__main__':
    print(format(pi,'.12g'))
    print(format(pi,'.2f'))

    print(0.1 + 0.1 + 0.1 == 0.3)
    print(round(0.1) + round(0.1) + round(0.1) == round(0.3))
    print(round(0.1,1) + round(0.1,1) + round(0.1,1) == round(0.3,1))
    print(round(0.1 + 0.1 + 0.1,10) == round(0.3,10))

    x = 3.14159
    print(x.as_integer_ratio())
    print(x.hex())
    print(x == float.fromhex('0x1.921f9f01b866ep+1'))

    print(sum([0.1] * 10) == 1.0)
    print(fsum([0.1] * 10) == 1.0)