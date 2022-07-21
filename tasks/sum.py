def sum(num):
    return num if num == 1 else num + sum(num - 1)

if __name__ == "__main__":
    print(sum(13))
