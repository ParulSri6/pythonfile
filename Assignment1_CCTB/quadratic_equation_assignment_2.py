import math


def solve_quadratic_equation():
    print("Solve Quadratic Equation")

    a = float(input("Enter a = "))
    b = float(input("Enter b = "))
    c = float(input("Enter c = "))

    if a == 0:
        print("Result:")
        print("This is not a valid quadratic equation")
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Result:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("Result:")
        print(f"x1 = x2 = {x}")
    else:
        print("Result:")
        print("There are no real solutions")


if __name__ == "__main__":
    solve_quadratic_equation()
