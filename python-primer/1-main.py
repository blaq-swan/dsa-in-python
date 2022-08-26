#!/usr/bin/python3
from solutions.is_multiple import is_multiple


if __name__ == "__main__":
    try:
        n = 20
        m = 5
        print(is_multiple(n, m))

        n = 3
        m = 5
        print(is_multiple(n, m))

        n = 0
        m = 5
        print(is_multiple(n, m))

        n = -5
        m = 0
        print(is_multiple(n, m))

    except Exception as e:
        print("Error!")
