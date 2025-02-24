#!/usr/bin/env python3
from sympy import log, simplify, N, Rational


def nested_radical(n):
    # Exactly compute √√…√2 with n square roots, which equals 2^(1/2^n)
    return 2 ** (Rational(1, 2**n))


def dirac_solution(n):
    # Dirac's formula: n = -log₂(log₂(nested_radical(n)))
    inner_log = log(nested_radical(n), 2)  # this is exactly 1/2^n
    return -log(inner_log, 2)


def main():
    # Test for n from 1 up to, say, 100
    for n in range(1, 100):
        expr = simplify(dirac_solution(n))
        # Evaluate with high precision to avoid any numerical pitfalls
        num = N(expr, 100)
        num = int(num)
        print(f"Dirac's expression with {n} nested radicals:")
        print("Symbolic:", expr)
        print("Numerical:", num)
        print()


if __name__ == "__main__":
    main()
