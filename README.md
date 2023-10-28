# Numerical Methods for Ordinary and Partial Differential Equations

# By: Czarmaigne De Guzman and Ralph Jayson Guinucud

# Newton-Raphson Method Documentation

This documentation provides an overview of the Python code that implements the Newton-Raphson method for finding approximate solutions to equations. The Newton-Raphson method is an iterative numerical technique used to find the roots of real-valued functions.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Code Structure](#code-structure)
4. [Functions](#functions)
    - [f_prime](#f_prime)
    - [f_doublePrime](#f_doublePrime)
    - [newton_raphson](#newton_raphson)
    - [convergent](#convergent)
    - [main](#main)
5. [Usage](#usage)
6. [Example](#example)

## Introduction <a name="introduction"></a>

The Newton-Raphson method is used to approximate the roots of a real-valued function. This method involves iteratively refining an initial guess until a sufficiently accurate solution is obtained. The algorithm relies on the first and second derivatives of the function.

## Prerequisites <a name="prerequisites"></a>

Before using this code, make sure you have the following prerequisites:

- Python installed (the code is written in Python 3).
- The SymPy library for symbolic mathematics. You can install it using `pip install sympy`.

## Code Structure <a name="code-structure"></a>

The code consists of several functions that work together to apply the Newton-Raphson method:

- `f_prime`: Computes the first derivative of the input equation.
- `f_doublePrime`: Computes the second derivative of the input equation.
- `newton_raphson`: Implements the Newton-Raphson iteration to find a root of the equation.
- `convergent`: Computes the convergence factor for the method.
- `main`: The main function that orchestrates the entire process.

## Functions <a name="functions"></a>

### `f_prime(equation)` <a name="f_prime"></a>

This function computes and returns the first derivative of the given equation.

### `f_doublePrime(equation)` <a name="f_doublePrime"></a>

This function computes and returns the second derivative of the given equation.

### `newton_raphson(equation, fprime, initial, tolerance)` <a name="newton_raphson"></a>

This function performs the Newton-Raphson iteration to find a root of the equation. It takes the following parameters:
- `equation`: The equation to solve.
- `fprime`: The first derivative of the equation.
- `initial`: The initial guess for the root.
- `tolerance`: The desired tolerance for the approximation.

### `convergent(equation, f_prime, f_doublePrime, initial)` <a name="convergent"></a>

This function calculates and returns the convergence factor for the Newton-Raphson method. It helps estimate the speed of convergence for the given equation.

### `main()` <a name="main"></a>

The `main` function is the entry point of the code. It collects user inputs for the equation to solve, tolerance, and initial guess. It then calls other functions to compute the first and second derivatives, calculate the convergence factor, and perform the Newton-Raphson iteration.

## Usage <a name="usage"></a>

To use this code:
1. Ensure that you have Python and the SymPy library installed.
2. Copy and paste the code into a Python file (e.g., `newton_raphson.py`).
3. Run the Python file.
4. Follow the prompts to input the equation, tolerance, and initial guess.

## Example <a name="example"></a>

Here is an example of how to use the code:

```python
Input an equation to solve using the Newton-Raphson method: x**3 - 2*x**2 - 5
First Derivative: 3*x**2 - 4*x
Second Derivative: 6*x - 4
Please input the tolerance for the equation: 1e-6
Please input initial value: 2.0

The convergent value is:  0.7777777777777778
For the value of x0: [2.0, 3.3636363636363638, 3.175457493870402, 3.1624105035691985, 3.1622776602211197, 3.162277660168379]
For the value of f(x0): [3.0, 1.3303449604195653, 0.03307987254723519, 0.000335202608532149, 1.6674885839939837e-07, 1.2079226507921703e-13]
For the value of f`(x0): [4.0, 7.353688572571959, 7.695685291791962, 7.701964046798546, 7.70195656424425, 7.701956564217932]
```

This example demonstrates how the code finds an approximate root of the equation `x^3 - 2x^2 - 5` using the Newton-Raphson method.


# Gauss-Jacobi Method Documentation

This documentation provides an overview of the Python code that implements the Gauss-Jacobi method for solving systems of linear equations. The Gauss-Jacobi method is an iterative technique used to approximate the solutions to a system of linear equations.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Code Structure](#code-structure)
4. [Functions](#functions)
    - [gauss_jacobi](#gauss_jacobi)
    - [test](#test)
    - [main](#main)
5. [Usage](#usage)
6. [Example](#example)

## Introduction <a name="introduction"></a>

The Gauss-Jacobi method is an iterative numerical technique used to solve systems of linear equations. It iteratively updates the values of the variables in the system until a convergence criteria (tolerance or maximum iterations) is met.

## Prerequisites <a name="prerequisites"></a>

Before using this code, make sure you have the following prerequisites:

- Python installed (the code is written in Python 3).
- The SymPy library for symbolic mathematics. You can install it using `pip install sympy`.

## Code Structure <a name="code-structure"></a>

The code consists of several functions that work together to apply the Gauss-Jacobi method:

- `gauss_jacobi`: Implements the Gauss-Jacobi iterative method to solve a system of linear equations.
- `test`: A function to test and print the diagonal elements of the coefficient matrix.
- `main`: The main function that collects user inputs for the system of equations, tolerance, and maximum iterations.

## Functions <a name="functions"></a>

### `gauss_jacobi(coeff_matrix, const_vector, tolerance, max_iterations)` <a name="gauss_jacobi"></a>

This function performs the Gauss-Jacobi iteration to solve a system of linear equations. It takes the following parameters:

- `coeff_matrix`: The coefficient matrix of the system of equations.
- `const_vector`: The constant vector on the right-hand side of the equations.
- `tolerance`: The desired tolerance for convergence.
- `max_iterations`: The maximum number of iterations to perform.

### `test()` <a name="test"></a>

This function is used to test and print the diagonal elements of the coefficient matrix. It is for diagnostic purposes.

### `main()` <a name="main"></a>

The `main` function is the entry point of the code. It collects user inputs for the system of equations, tolerance, and maximum iterations, and then calls the `gauss_jacobi` function to solve the system.

## Usage <a name="usage"></a>

To use this code:

1. Ensure that you have Python and the SymPy library installed.
2. Copy and paste the code into a Python file (e.g., `gauss_jacobi.py`).
3. Run the Python file.
4. Follow the prompts to input the system of linear equations, tolerance, and maximum iterations.

## Example <a name="example"></a>

Here is an example of how to use the code:

```python
This program solves a system of linear equations using the Gauss-Jacobi method with SymPy.
Enter the number of equations: 3
Enter the equations in the form 'a1*x1 + a2*x2 + ... + an*xn = b':
Enter equation 1: 4*x1 - x2 - x3 = 7
x1 - x2 - x3 = 3
4*x1 - 2*x2 + x3 = 1
[[4, -1, -1], [1, -1, -1], [4, -2, 1]]
[7, 3, 1]
Enter the tolerance for convergence: 1e-6
Enter the maximum number of iterations: 20
[2.0]
[2.0]
[2.0]
Solution found:
x1 = 2.00000000000000
x2 = 2.00000000000000
x3 = 2.00000000000000
```

This example demonstrates how the code uses the Gauss-Jacobi method to solve a system of linear equations, producing the solution `[2.0, 2.0, 2.0]`.




# Newton Interpolation Method Documentation

This documentation provides an overview of the Python code that implements the Newton Interpolation method for constructing and evaluating interpolation polynomials. The Newton Interpolation method is a mathematical technique used to approximate a function using a polynomial that passes through a set of given data points.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Code Structure](#code-structure)
4. [Functions](#functions)
    - [newton_interpolation](#newton_interpolation)
    - [main](#main)
5. [Usage](#usage)
6. [Example](#example)

## Introduction <a name="introduction"></a>

The Newton Interpolation method is used to find an interpolating polynomial that fits a set of data points. It is particularly useful in numerical analysis and data approximation.

This code demonstrates the Newton Interpolation method using the SymPy library for symbolic mathematics.

## Prerequisites <a name="prerequisites"></a>

Before using this code, make sure you have the following prerequisites:

- Python installed (the code is written in Python 3).
- The SymPy library for symbolic mathematics. You can install it using `pip install sympy`.

## Code Structure <a name="code-structure"></a>

The code consists of several functions that work together to perform Newton Interpolation:

- `newton_interpolation`: Computes the interpolation polynomial based on a set of data points.
- `main`: The main function that collects user inputs, calculates the interpolation polynomial, and evaluates it at a specified value of `x`.

## Functions <a name="functions"></a>

### `newton_interpolation(data_points)` <a name="newton_interpolation"></a>

This function constructs an interpolation polynomial that passes through a set of data points. It takes the following parameters:
- `data_points`: A list of data points in the form of (x, y) pairs.

### `main()` <a name="main"></a>

The `main` function serves as the entry point for the code. It collects user inputs for the data points and the value of `x` for interpolation. It also orchestrates the interpolation process.

## Usage <a name="usage"></a>

To use this code:

1. Ensure that you have Python and the SymPy library installed.
2. Copy and paste the code into a Python file (e.g., `newton_interpolation.py`).
3. Run the Python file.
4. Follow the prompts to enter data points as (x, y) pairs and specify the value of `x` for interpolation.

## Example <a name="example"></a>

Here is an example of how to use the code:

```python
Enter data points as (x, y) pairs. Enter 'done' to finish.
Enter a data point (x, y): 1.0 2.0
Enter a data point (x, y): 2.0 3.0
Enter a data point (x, y): 3.0 6.0
Enter a data point (x, y): done

Interpolation Polynomial:
2.0 + 1.0*x*(-1.0 + 3.0*x)

Enter a value of x for interpolation: 2.5
Interpolated value at x = 2.5: y = 3.50000000000000
```

This example demonstrates how to use the code to calculate an interpolation polynomial that fits a set of data points and then evaluate the polynomial at a specific value of `x`.


# Secant Method Documentation

This documentation provides an overview of the Python code that implements the Secant method for finding approximate solutions to equations. The Secant method is an iterative numerical technique used to find the roots of real-valued functions.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Code Structure](#code-structure)
4. [Functions](#functions)
    - [secant_method](#secant_method)
5. [Usage](#usage)
6. [Example](#example)

## Introduction <a name="introduction"></a>

The Secant method is a root-finding algorithm that is similar to the Newton-Raphson method but does not require the evaluation of derivatives. It is a useful technique for finding an approximate root of a real-valued function.

This code demonstrates the Secant method using the SymPy library for symbolic mathematics.

## Prerequisites <a name="prerequisites"></a>

Before using this code, make sure you have the following prerequisites:

- Python installed (the code is written in Python 3).
- The SymPy library for symbolic mathematics. You can install it using `pip install sympy`.

## Code Structure <a name="code-structure"></a>

The code consists of a single function and an entry point for user interaction:

- `secant_method`: Implements the Secant method to find an approximate root of the equation.
- User interaction: The code asks the user for the equation and initial guesses.

## Functions <a name="functions"></a>

### `secant_method(func, x0, x1, tol=1e-6, max_iter=100)` <a name="secant_method"></a>

This function performs the Secant method to find an approximate root of the given equation. It takes the following parameters:
- `func`: The target function to find the root of (as a SymPy expression).
- `x0`: The first initial guess.
- `x1`: The second initial guess.
- `tol`: The desired tolerance for the approximation (default is 1e-6).
- `max_iter`: The maximum number of iterations allowed (default is 100).

## Usage <a name="usage"></a>

To use this code:

1. Ensure that you have Python and the SymPy library installed.
2. Copy and paste the code into a Python file (e.g., `secant_method.py`).
3. Run the Python file.
4. Follow the prompts to enter the equation and initial guesses for the Secant method.

## Example <a name="example"></a>

Here is an example of how to use the code:

```python
Enter the equation in terms of 'x': x**3 - 2*x**2 - 5
Enter the first initial guess (x0): 1
Enter the second initial guess (x1): 2

Approximate root: 2.16971579393822
```

This example demonstrates how to use the code to find an approximate root of the equation `x^3 - 2x^2 - 5` using the Secant method. The code prompts the user for the equation and initial guesses and returns the approximate root.


# Simpson's Rule Numerical Integration

This is a Python script that implements Simpson's Rule for numerical integration. Simpson's Rule is a numerical method for approximating the definite integral of a function over a specified interval. It provides a more accurate approximation compared to the simpler trapezoidal rule.

## Usage
To use this script, follow these steps:

1. Clone or download this repository to your local machine.

2. Run the `simpsons_rule.py` script.

```bash
python simpsons_rule.py
```

3. Follow the prompts to input the following parameters:

   - Lower limit of integration (a)
   - Upper limit of integration (b)
   - Number of intervals (n, must be even)
   - Function f(x) to be integrated (as a Python lambda function)

4. The script will then calculate and display the approximate integral of the function using Simpson's Rule.

## Example
Here's an example of how to use the script:

```
Enter the lower limit of integration (a): 0
Enter the upper limit of integration (b): 1
Enter the number of intervals (n, must be even): 4
Enter the function f(x) (e.g., x**2): x**2

The approximate integral is: 0.3333
```

## Note
- Ensure that the number of intervals (n) is even; Simpson's Rule requires an even number of intervals.
- Input the function as a valid Python lambda function. For example, to integrate `x^2`, input `x**2`.

## License
This script is provided under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

# 3/8 Simpson's Rule Numerical Integration

This is a Python script that implements the 3/8 Simpson's Rule for numerical integration. The 3/8 Simpson's Rule is a numerical method for approximating the definite integral of a function over a specified interval, which is especially useful when the number of intervals is a multiple of 3.

## Usage
To use this script, follow these steps:

1. Clone or download this repository to your local machine.

2. Run the `simpsons_3_8_rule.py` script.

```bash
python simpsons_3_8_rule.py
```

3. Follow the prompts to input the following parameters:

   - Lower limit of integration (a)
   - Upper limit of integration (b)
   - Number of intervals (n, must be a multiple of 3)
   - Function f(x) to be integrated (as a Python lambda function)

4. The script will then calculate and display the approximate integral of the function using 3/8 Simpson's Rule.

## Example
Here's an example of how to use the script:

```
Enter the lower limit of integration (a): 0
Enter the upper limit of integration (b): 1
Enter the number of intervals (n, must be a multiple of 3): 6
Enter the function f(x): x**2

Simpson's 3/8 Rule Calculation:
Interval    f(a)    f(a+h)    f(a+2h)    f(a+3h)    f(a+3h)    Subtotal
0           0       0.16666666666666666    0.6666666666666666    1.5     1.5
1           1.5     3.0     4.5     6.0     15.0
2           15.0    24.0    33.0    42.0    114.0

The approximate integral is: 3.0000
```

## Note
- Ensure that the number of intervals (n) is a multiple of 3; 3/8 Simpson's Rule requires this condition.
- Input the function as a valid Python lambda function. For example, to integrate `x^2`, input `x**2`.

## License
This script is provided under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

# Numerical Differentiation with Richardson Extrapolation

This Python script uses Richardson Extrapolation to numerically approximate the derivative of a function at a given point. It applies the forward difference method with increasing accuracy by successively reducing the step size. Richardson Extrapolation is employed to enhance the precision of the derivative approximation.

## Usage

1. Make sure you have the `sympy` library installed. You can install it using `pip`:

   ```bash
   pip install sympy
   ```

2. Copy and paste the code into a Python environment or script.

3. Modify the input parameters, if necessary:

   - `x_value`: The point at which you want to calculate the derivative.
   - `h_value`: The initial step size for differentiation.
   - `n_value`: The number of extrapolation steps (higher values provide greater accuracy).

4. Run the script:

   ```bash
   python your_script_name.py
   ```

The script will calculate and display the derivative at the specified point using Richardson Extrapolation.

## Example

Here's an example of how to use the script:

```python
# Input parameters
x_value = 2.0  # The point at which you want to calculate the derivative
h_value = 0.1  # Initial step size
n_value = 3  # Number of extrapolation steps

# Calculate the derivative using Richardson Extrapolation
result = richardson_extrapolation(f, x_value, h_value, n_value)

print(f"The derivative at x = {x_value} is approximately: {result:.8f}")
```

## Note

- Ensure you have the `sympy` library installed to use symbolic mathematics.
- Adjust `x_value`, `h_value`, and `n_value` as needed for your specific differentiation problem.
- Richardson Extrapolation is used to improve accuracy by successively halving the step size.

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.


# Numerical Differentiation with Richardson Extrapolation (Central Difference)

This Python script uses Richardson Extrapolation to numerically approximate the derivative of a function at a given point. It employs the central difference method for differentiation, which provides improved accuracy compared to the forward difference method. Richardson Extrapolation enhances the precision of the derivative approximation.

## Usage

1. Make sure you have the `sympy` library installed. You can install it using `pip`:

   ```bash
   pip install sympy
   ```

2. Copy and paste the code into a Python environment or script.

3. Modify the input parameters, if necessary:

   - `x_value`: The point at which you want to calculate the derivative.
   - `h_value`: The initial step size for differentiation.
   - `n_value`: The number of extrapolation steps (higher values provide greater accuracy).

4. Run the script:

   ```bash
   python your_script_name.py
   ```

The script will calculate and display the derivative at the specified point using Richardson Extrapolation with central difference differentiation.

## Example

Here's an example of how to use the script:

```python
# Input parameters
x_value = 2.0  # The point at which you want to calculate the derivative
h_value = 0.1  # Initial step size
n_value = 3  # Number of extrapolation steps

# Calculate the derivative using Richardson Extrapolation with central difference differentiation
result = richardson_extrapolation(f, x_value, h_value, n_value)

print(f"The derivative at x = {x_value} is approximately: {result:.8f}")
```

## Note

- Ensure you have the `sympy` library installed to use symbolic mathematics.
- Adjust `x_value`, `h_value`, and `n_value` as needed for your specific differentiation problem.
- Central difference differentiation is used to improve accuracy by taking the difference of function values at nearby points.
- Richardson Extrapolation is applied to enhance the precision of the derivative approximation.

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.
