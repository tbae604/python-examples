def get_fibonacci(n, a=None, b=None):
    """
    Takes integer n and returns nth number of Fibonacci sequence
    i.e. x_n = x_(n-1) + x_(n-2)
    """
    if a == None and b == None:
        a, b = 0, 1
    if n == 0:
        return a
    else:
        # Add steps along descending sequence
        a, b = b, a + b
        # Then reduce towards zero
        n = n - 1
        return get_fibonacci(n, a, b)

if __name__ == "__main__":
    n = int(raw_input("Please provide n to calculate nth Fibonacci number:\n"))
    print("Result: {0}".format(get_fibonacci(n)))