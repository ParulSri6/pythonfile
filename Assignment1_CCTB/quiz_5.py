def list_squares(input_function=input):
    numbers = []
    while True:
        try:
            user_input = input_function("Enter a positive integer: ")
            if user_input.isdigit():  # Check if input is a positive integer
                number = int(user_input)
                if number < 0:
                    print("Negative number entered, stopping program.")
                    break
                elif number == 0:
                    print("Zero entered, stopping input.")
                    break
                else:
                    numbers.append(number)
                    print(f"{number} {number ** 2}")  # Print the number and its square
            else:
                raise ValueError("Invalid input, please enter a positive integer.")
        except ValueError as ve:
            print(f"Error message: {ve}")

    # Print all numbers and their squares at the end
    print("Numbers and their squares:")
    for num in numbers:
        print(f"{num} {num ** 2}")


if __name__ == "__main__":
    list_squares()
