# Numerical Methods for Ordinary and Partial Differential Equations

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

