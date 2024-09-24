# URL: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def print_formatted(number):
    # your code goes here
    space = len(bin(number)) # binary in string format '0b10101'
    for i in range(1, number + 1):
        print(
            f"{str(i).rjust(space - 2)}{oct(i)[2:].rjust(space - 1)}"
            f"{hex(i).upper()[2:].rjust(space - 1)}{bin(i)[2:].rjust(space - 1)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
