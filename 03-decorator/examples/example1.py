import time


def measure_time(fn):

    def decorator(*args, **kwargs):
        start = time.time()

        res = fn(*args, **kwargs)

        elapsed = time.time() - start
        print fn.__name__, "took", elapsed, "seconds"

        return res

    return decorator


def _sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


@measure_time
def python_decorated_sum(a, b):
    total = 0

    for i in range(10000000):
        total += a + b

    return total


def main():

    print "Non decorated sum"
    print _sum(4, 5)

    print "\nDecorated sum"
    print measure_time(_sum)(4, 5)

    print "\nPython decorated sum"
    print python_decorated_sum(4, 5)

if __name__ == '__main__':
    main()
