def simpsons_rule(a, b, n, func):
    if n % 2 != 0:
        raise ValueError("n must be an even number for Simpson's Rule")

    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n, 2):
        result += 4 * func(a + i * h)

    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)

    result *= h / 3
    return result

if __name__ == "__main__":
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    n = int(input("Enter the number of intervals (n, must be even): "))

    # Input the function as a lambda function
    func_str = input("Enter the function f(x) (e.g., x**2): ")
    func = lambda x: eval(func_str)

    integral = simpsons_rule(a, b, n, func)
    print(f"The approximate integral is: {integral:.4f}")
