import sys


def reverse(s):
    return s[::-1]


def main():
    s = input('please enter the input string:\n')
    print(reverse(s))
    return 0


if __name__ == "__main__":
    sys.exit(main())
