from collections import OrderedDict

divisors = OrderedDict()
divisors[3] = "my"
divisors[5] = "theresa"
divisors[7] = "clothes"


def create_string(num):
    result = ""
    for divisor in divisors:
        if is_divisible(num, divisor):
            result += (divisors[divisor])
    print(result)

    if result == '':
        print(num)


def is_divisible(num, divisor):
    if num % divisor == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    create_string(99)
