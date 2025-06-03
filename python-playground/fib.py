# Recursion
# The Fibonacci sequence is a sequence of numbers that can be calculated recursively.
# https://en.wikipedia.org/wiki/Fibonacci_sequence


def factorial(n):
    # Starting condition (base case)
    if n == 0:
        return 1
    else:
        # Calculation of next value
        return n * factorial(n - 1)


def main():
    f0 = 0
    f1 = 1
    print("\nA factorial expansion is easily created in Python: ")
    print("(and is simpler than Fibonacci)")

    print(f"Recurively, 5! = {factorial(5)}")
    print("\nSolution for Fibonacci is at https://www.geeksforgeeks.org/recursion-in-python/")

if __name__ == "__main__":
    main()
