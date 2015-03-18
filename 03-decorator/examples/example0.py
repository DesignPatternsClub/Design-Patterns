import time


def _sum(a, b):
    total = 0

    start = time.time()

    for i in range(10000000):
        total += a + b

    elapsed = time.time() - start
    print "_sum took", elapsed, "seconds"

    return total


def main():

    print "Non decorated sum"
    print _sum(4, 5)


if __name__ == '__main__':
    main()
