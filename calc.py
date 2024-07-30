# factorial and reverse_number functions

def factorial():
    number = int(input("Enter a number: "))
    if number < 0:
        print("The factorial of negative numbers is not defined.")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        print(f"The factorial of {number} is {result}")


def reverse_number():
    number = int(input("Enter a number: "))
    actual_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    print(f"The reversed number is {reversed_number}")


if __name__ == "__main__":
    factorial()
    reverse_number()
