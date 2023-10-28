import sympy as sp

# Define the symbol and the function
x = sp.symbols('x')
f = 0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

# Forward Difference Differentiation
def forward_difference(f, x, h):
    return (f.subs(x, x + h) - f.subs(x, x)) / h

# Richardson Extrapolation
def richardson_extrapolation(f, x, h, n):
    D = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        h_i = h / (2**i)
        D[i][0] = forward_difference(f, x, h_i)
    
    print(f"| Step | h (Step Size) | f'(x) (Approximation) |")
    print("|------|---------------|------------------------|")
    
    for j in range(1, n):
        for i in range(n - j):
            D[i][j] = D[i+1][j-1] + (D[i+1][j-1] - D[i][j-1]) / (4**j - 1)
            print(f"| {j} | {h / (2**j):.8f} | {D[i][j]:.8f} |")
    
    return D[0][n-1]

# Input parameters
x_value = 2.0  # The point at which you want to calculate the derivative
h_value = 0.1  # Initial step size
n_value = 3  # Number of extrapolation steps

# Calculate the derivative using Richardson Extrapolation
result = richardson_extrapolation(f, x_value, h_value, n_value)

print(f"The derivative at x = {x_value} is approximately: {result:.8f}")
