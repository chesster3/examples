"""
Будем говорить, что число a лучше числа b, если сумма цифр a больше
суммы цифр числа b, а в случае равенства сумм их цифр, если число a
меньше числа b. Например, число 124 лучше числа 123, так как у
первого из них сумма цифр равна семи, а у второго – шести. Также,
число 3 лучше числа 111, так как у них равны суммы цифр, но первое
из них меньше.

Дано число n. Найдите такой его делитель (само число n и единица
считаются делителями числа n), который лучше любого другого делителя
числа n.
"""

def find_all_divs(n):
    res = []
    for div in range(1, n+1):
        num = n % div
        if num == 0:
            res.append(div)
    return res


def find_best_div(n):
    divs = find_all_divs(n)
    best = max_sum = 0
    for n in divs:
        sum = 0
        for s in list(str(n)):
            sum += int(s)

        if sum >= max_sum:
            max_sum = sum
            best = n
    return best


def check_answer():
    if find_best_div(10) == 5:
        print("Right answer for 10")
    if find_best_div(239) == 239:
        print("Right answer for 239")


if __name__ == "__main__":
    check_answer()
