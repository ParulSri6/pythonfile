def get_two_numbers_and_calculate():
    # Input two numbers
    a = int(input("Enter the first number a = "))
    b = int(input("Enter b = "))

    # Calculate sum, multiplication, and division
    sum_result = a + b
    multiplication_result = a * b
    division_result = a / b
    # Convert float to integer for division
    if division_result.is_integer():
        division_result = int(division_result)

    # Print results
    print("\nResults:")
    print(f"Sum is {sum_result}")
    print(f"Multiplication is {multiplication_result}")
    print(f"Division is {division_result}")


def calculate_seconds_from_days():
    days = int(input("\nEnter the number of days: "))
    seconds = days * 24 * 60 * 60
    print(f"{days} days have {seconds} seconds")


if __name__ == "__main__":
    get_two_numbers_and_calculate()
    calculate_seconds_from_days()
