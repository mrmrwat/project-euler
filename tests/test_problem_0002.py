from euler.lib import even, fibonacci
from euler.problems.problem_0002 import main as problem


PROBLEM_TEXT = """
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""


def test_example():
    expected_fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    expected_even_list = [2, 8, 34]
    expected_even_sum = 44

    fib_list = list(fibonacci(1, 2, terms=10))
    assert fib_list == expected_fib_list
    even_list = list(even(fib_list))
    assert even_list == expected_even_list
    even_sum = sum(even_list)
    assert even_sum == expected_even_sum


def test_answer():
    answer = problem()
    assert answer == 4613732