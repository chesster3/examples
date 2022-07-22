def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    s1 = "mamam"
    s2 = "photo"
    if is_palindrome(s1):
        print("Is pal")
    else:
        print("It's not")
