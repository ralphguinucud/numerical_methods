import sympy as sp

def newton_interpolation(data_points):
    x = sp.Symbol('x')
    
    # Create a list to store the coefficients of the interpolation polynomial
    coefficients = []
    
    # Initialize the coefficients with the y-values from the data points
    for point in data_points:
        coefficients.append(point[1])
    
    n = len(data_points)
    
    # Calculate the divided differences
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coefficients[j] = (coefficients[j] - coefficients[j - 1]) / (data_points[j][0] - data_points[j - i][0])
    
    # Build the interpolation polynomial
    interpolation_poly = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - data_points[j][0])
        interpolation_poly += term
    
    return interpolation_poly

def main():
    # Initialize an empty list for data points
    data_points = []
    
    print("Enter data points as (x, y) pairs. Enter 'done' to finish.")
    
    while True:
        input_str = input("Enter a data point (x, y): ")
        
        # Check if the user wants to exit data input
        if input_str.lower() == 'done':
            break
        
        try:
            x, y = map(float, input_str.split())
            data_points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter data points in the format 'x y'. Example: 1.0 2.5")
    
    if len(data_points) < 2:
        print("At least two data points are required for interpolation.")
        return
    
    # Calculate the interpolation polynomial
    interpolation_poly = newton_interpolation(data_points)
    
    print("Interpolation Polynomial:")
    print(interpolation_poly)
    
    # Prompt the user for a value of x to interpolate at
    x_value = float(input("Enter a value of x for interpolation: "))
    
    # Substitute the x value into the interpolation polynomial to find the corresponding y value
    y_value = interpolation_poly.subs('x', x_value)
    
    print(f"Interpolated value at x = {x_value}: y = {y_value}")

if __name__ == "__main__":
    main()


