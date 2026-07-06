def add(a, b):
    """Return the sum of a and b."""
    return a + b
result = add(20, 30)
print(result)

num1 = 5
num2 = 10
sum = num1 + num2

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python addition.py <a> <b>")
    else:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
        except ValueError:
            print("Please provide two numeric values.")
        else:
            print(add(a, b))
