import sys


def reverse_each_word(s):
    result = ''
    tmp = ''
    for ch in s:
        if ch.isalpha():
            tmp += ch
        else:
            result += tmp[::-1] + ch
            tmp = ''
    result += tmp[::-1]

    return result


def main():
    s = input('please enter the input string:\n')
    print(reverse_each_word(s))

    return 0


if __name__ == "__main__":
    sys.exit(main())
