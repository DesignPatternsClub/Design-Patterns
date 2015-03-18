import time


class MeasureTime(object):

    """Decorator object."""

    def __init__(self, *args):
        self.args = args

    def __call__(self, fn):

        def wrapped_fn(*fn_args):
            start = time.time()

            res = fn(*fn_args)

            elapsed = time.time() - start
            print fn.__name__, "took", elapsed, "seconds"

            return res + self.args[0]
        return wrapped_fn


def _sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


@MeasureTime(2222)
def python_decorated_sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


def main():

    print "Non decorated sum"
    print _sum(4, 5)

    print "\nDecorated sum"
    print MeasureTime(2222)(_sum)(4, 5)

    print "\nPython decorated sum"
    print python_decorated_sum(4, 5)

if __name__ == '__main__':
    main()
