import cmath

def solve_quadratic_complex(a, b, c):
    discriminant = b**2 - 4*a*c # Calculate the discriminant
    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)# Use cmath.sqrt to handle negative numbers
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {x1} and {x2}")
    return x1, x2

# Example: x^2 + 1x + 1 = 0 (This has no real roots)
solve_quadratic_complex(1, 1, 1)