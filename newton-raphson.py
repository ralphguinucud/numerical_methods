import sympy

def f_prime(equation):
   x = sympy.Symbol('x')
   return sympy.diff(equation, x)

def f_doublePrime(equation):
    x = sympy.Symbol('x')
    return sympy.diff(f_prime(equation), x)

def newton_raphson(equation, fprime, initial, tolerance):
    x = sympy.Symbol('x')
    initial_values = [initial]
    functionEquation_values = [equation.subs(x, initial)]
    functionPrime_values = [fprime.subs(x, initial)]
    counter = 0
    while float(abs(equation.subs(x, initial))) > tolerance:
        counter = counter + 1
        x1 = initial - equation.subs(x, initial) / fprime.subs(x, initial)
        initial = x1
        initial_values.append(initial)
        functionEquation_values.append(equation.subs(x, initial))
        functionPrime_values.append(fprime.subs(x,initial))
        if(counter > 100):
            print('This is the maximum iteration.')
            break
    
    print('For the value of x0:', initial_values)
    print('For the value of f(x0):', functionEquation_values)
    print('For the value of f`(x0):', functionPrime_values)
    return True
def convergent(equation, f_prime, f_doublePrime, initial):
    x = sympy.Symbol('x')
    return abs((equation.subs(x, initial) * f_doublePrime.subs(x, initial) / f_prime.subs(x, initial)**2 ))

def main():    
    equation_str = input('Input an equation to solve using the Newton-Raphson method: ')
#   make a if statement to validate equation
    equation = sympy.sympify(equation_str)
    f_prime_eq = f_prime(equation)
    f_doublePrime_eq = f_doublePrime(equation)
    print(f'First Derivative: {f_prime_eq}')
    print(f'Second Derivative: {f_doublePrime_eq}')
    tolerance_str = input('Please input the tolerance for the equation: ')
        # Try to convert the user input to a float, handling scientific notation
    try:
        tolerance = float(tolerance_str)
    except ValueError:
        # If conversion fails, attempt to parse scientific notation
        try:
            tolerance = float(tolerance_str.replace('e', 'E'))
        except ValueError:
            print('Invalid tolerance input. Please use numeric format (e.g., 1e-6).')
            return
    initial = float(input('please input initial value: '))
# compute convergent
    convergent_eq = convergent(equation, f_prime_eq, f_doublePrime_eq, initial)
    print("The convergent value is: ",convergent_eq)

# iteration of the equation
    newton_raphson(equation, f_prime_eq, initial, tolerance)


if __name__ == "__main__":
  main()