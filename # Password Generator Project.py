#Password Generator Project
import random
import secrets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters, nr_symbols, nr_numbers):
    """Generates a password with specified character counts and randomized order."""
    password_list = []
    for _ in range(nr_letters + nr_symbols + nr_numbers):
        category = secrets.choice(["letters", "symbols", "numbers"])
        password_list.append(secrets.choice(globals()[category]))
    random.shuffle(password_list)
    return "".join(password_list)

while True:
    try:
        nr_letters = int(input("How many letters would you like in your password? "))
        nr_symbols = int(input(f"How many symbols would you like? "))
        nr_numbers = int(input(f"How many numbers would you like? "))

        password = generate_password(nr_letters, nr_symbols, nr_numbers)

        # Add optional password strength checks here

        print(f"Your password is: {password}")
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
