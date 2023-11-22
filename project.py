import random
import string


def generate_password(
    length,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special_chars=True,
):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "No characters selected for password generation."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def get_password_options(use_uppercase, use_lowercase, use_digits, use_special_chars):
    return use_uppercase, use_lowercase, use_digits, use_special_chars


def get_password_length(length):
    if length.isdigit() and int(length) > 0:
        return int(length)
    else:
        raise ValueError("Invalid password length. Please enter a positive integer.")


def generate_password_with_options(
    length, use_uppercase, use_lowercase, use_digits, use_special_chars
):
    password = generate_password(
        length, use_uppercase, use_lowercase, use_digits, use_special_chars
    )
    return password

def main():
    length = input("Enter password length: ")
    use_uppercase = input("Include uppercase letters (y/n): ").lower() == "y"
    use_lowercase = input("Include lowercase letters (y/n): ").lower() == "y"
    use_digits = input("Include digits (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters (y/n): ").lower() == "y"

    try:
        password_length = get_password_length(length)
        options = get_password_options(
            use_uppercase, use_lowercase, use_digits, use_special_chars
        )
        password = generate_password_with_options(password_length, *options)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

