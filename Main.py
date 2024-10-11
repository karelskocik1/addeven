def is_even_or_odd(number):
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


# Loop for user input with exception handling
while True:
    user_input = input("Enter a number (or 'Q' to quit): ")
    if user_input.upper() == 'Q':
        print("Exiting the program. Goodbye!")
        break
    try:
        number = int(user_input)
        print(is_even_or_odd(number))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
