import sys


def count(n):
    result = 0
    for i in range(1, n + 1):
        if i % 15 == 0 or (i % 3 != 0 and i % 5 != 0):
            result += 1

    return result


def main():
    n = int(input('please input a positive integer: '))
    if n < 1:
        print('input is not positive')
        return -1

    print(count(n))

    return 0


if __name__ == "__main__":
    sys.exit(main())
