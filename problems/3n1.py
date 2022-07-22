"""
Рассмотрим следующий алгоритм генерации последовательности: начните с целого числа n, если n четное, разделите его на 2; если n нечетное, умножьте на 3 и добавьте 1. Повторите вышеуказанные шаги с новым полученным значением до n = 1 и остановитесь. Например, когда n = 22, алгоритм генерирует следующую последовательность:
22，11，34，17，52，26，13，40，20，10，5，16，8，4，2，1
Люди предполагают (не доказано), что для любого целого числа n алгоритм всегда заканчивается на n = 1. Эта гипотеза верна как минимум для целых чисел в пределах 1 000 000.
"""

import unittest as ut

def is_even(n):
    return (n & 1) == 0

def calculate(n):
    # n >> 1 == n / 2, but faster. For even nums it's fine
    return n >> 1 if is_even(n) else (n*3) + 1

# return a list with sequance of nums
def algo(n):
    num, res = n, [n]
    while num > 1:
        num = calculate(num)
        res.append(num)
    return res

# Checking result
class TestResult(ut.TestCase):
    def test_result(self):
        right_answer = [22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]
        my_answer = algo(22)
        self.assertEqual(my_answer, right_answer)

def check_result(res):
    right_answer = [22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]
    return res == right_answer


if __name__ == "__main__":
    is_right = check_result(algo(22))
    print("Right answer" if is_right else "It's wrong :(")
