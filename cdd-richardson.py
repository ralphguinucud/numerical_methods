import sympy as sp

# Define the symbol and the function
x = sp.symbols('x')
f = 0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

# Central Difference Differentiation
def central_difference(f, x, h):
    return (f.subs(x, x + h) - f.subs(x, x - h)) / (2 * h)

# Richardson Extrapolation
def richardson_extrapolation(f, x, h, n):
    for i in range(n):
        h_i = h / (2**i)
        approx = central_difference(f, x, h_i)
        print(f"Step {i + 1}: h = {h_i:.8f}, Approximation = {approx:.8f}")
    
    return approx

# Input parameters
x_value = 2.0  # The point at which you want to calculate the derivative
h_value = 0.1  # Initial step size
n_value = 3  # Number of extrapolation steps

# Calculate the derivative using Richardson Extrapolation with CDD
result = richardson_extrapolation(f, x_value, h_value, n_value)

print(f"The derivative at x = {x_value} is approximately: {result:.8f}")
