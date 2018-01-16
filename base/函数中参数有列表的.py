import sys
import copy

def f(x, l1=[]):
    for i in range(x):
        l1.append(i*i)
    print(l1)


def f1(var1, var2=None):
    if not var2:
        var2 = []
    for i in range(var1):
        var2.append(i * i)
    print(var2)


if __name__ == '__main__':
    f(2)
    f(3, [3, 2, 1])
    f(3)
    print(sys.getrefcount(f))

    f1(2)
    f1(3, [3, 2, 1])
    f1(3)
    print(sys.getrefcount(f1))

    a = [1, 2, 3]
    print(sys.getrefcount(a))
    b = a
    e = a
    print(sys.getrefcount(a))
    print(sys.getrefcount(b))
    c = copy.deepcopy(a)
    print(sys.getrefcount(a))
    print(sys.getrefcount(c))