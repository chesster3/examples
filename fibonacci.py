def print_fib_nums(n1, n2, length):
    if n1 <= length:
        print(n1)
        print_fib_nums(n2, n1 + n2, length)

if __name__ == "__main__":
    print_fib_nums(0,1, 1202400)
