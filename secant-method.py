import sympy as sp

def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = func

    for i in range(max_iter):
        f_x0 = f.subs(x, x0).evalf()
        f_x1 = f.subs(x, x1).evalf()

        if abs(f_x1) < tol:
            return x1

        if abs(f_x0 - f_x1) < tol:
            return x0

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_new

    raise ValueError("Secant method did not converge")

if __name__ == "__main__":
    x = sp.symbols('x')
    
    # Ask the user for the equation as input
    equation = input("Enter the equation in terms of 'x': ")
    
    try:
        # Parse the user's input into a SymPy expression
        target_function = sp.sympify(equation)
        
        x0 = float(input("Enter the first initial guess (x0): "))
        x1 = float(input("Enter the second initial guess (x1): "))
        
        root = secant_method(target_function, x0, x1)
        print(f"Approximate root: {root}")
    except (ValueError, sp.SympifyError) as e:
        print("Invalid input. Please enter a valid equation and initial guesses.")
