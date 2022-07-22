def sort(m, n):
    return (m, n) if m > n else (n, m)

def euclid_algo(m, n):
    while m != n:
        m, n = sort(m, n)
        m -= n
    return m



if __name__ == "__main__":
    print(euclid_algo(28, 14))
