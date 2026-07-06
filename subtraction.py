def subtract(a, b):
    """Return the result of a - b.

    Works for numbers and objects that implement __sub__.
    """
    return a-b


if __name__ == "__main__":
    # simple self-test
    result = subtract(50, 20)
    print(subtract(50, 20))