def simpsons_3_8_rule(a, b, n, func):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for 3/8 Simpson's Rule")

    h = (b - a) / n
    result = func(a) + func(b)

    table = []
    table.append(["Interval", "f(a)", "f(a+h)", "f(a+2h)", "f(a+3h)", "Subtotal"])

    for i in range(0, n, 3):
        a_i = a + i * h
        subtotal = (func(a_i) + 3 * (func(a_i + h) + func(a_i + 2 * h)) + func(a_i + 3 * h))
        result += subtotal
        table.append([i // 3, func(a_i), func(a_i + h), func(a_i + 2 * h), func(a_i + 3 * h), subtotal])

    result *= 3 * h / 8

    print("Simpson's 3/8 Rule Calculation:")
    for row in table:
        print("\t".join(str(entry) for entry in row))

    return result

if __name__ == "__main__":
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    
    while True:
        try:
            n = int(input("Enter the number of intervals (n, must be a multiple of 3): "))
            if n % 3 == 0:
                break
            else:
                print("Error: n must be a multiple of 3. Please enter a valid value.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer value for n.")

    func_str = input("Enter the function f(x): ")

    # Create a lambda function to evaluate the user-provided function
    func = lambda x: eval(func_str)

    integral = simpsons_3_8_rule(a, b, n, func)
    print(f"The approximate integral is: {integral:.4f}")
