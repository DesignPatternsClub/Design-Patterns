import time


class MeasureTime(object):

    """Decorator object."""

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):

        start = time.time()

        res = self.fn(*args)

        elapsed = time.time() - start
        print self.fn.__name__, "took", elapsed, "seconds"

        return res


def _sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


@MeasureTime
def python_decorated_sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


def main():

    print "Non decorated sum"
    print _sum(4, 5)

    print "\nDecorated sum"
    print MeasureTime(_sum)(4, 5)

    print "\nPython decorated sum"
    print python_decorated_sum(4, 5)

if __name__ == '__main__':
    main()
