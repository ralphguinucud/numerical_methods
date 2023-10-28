# 1/3 Simpson's Rule Numerical Integration

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

 

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.
