# Password Generator

## [Demo](https://farid-malekpour.github.io/password-generator)

#### Video Demo: (https://youtu.be/MbnOJOEfQKc)

#### Description:
The Password Generator is a Python application that allows users to generate secure passwords with customizable options. It provides a simple command-line interface for generating passwords based on user-defined criteria, such as length and character types (uppercase letters, lowercase letters, digits, and special characters).

#### Test Suite (test_pgen.py)
The `test_project.py` file contains a suite of pytest tests to ensure the correctness of the functions in `project.py`. These tests cover various scenarios to verify that the password generation and validation functions work as expected.


### Usage
1. The program will prompt you to enter the desired password length.
2. You can choose to include or exclude the following character types in your password:
- Uppercase Letters
- Lowercase Letters
- Digits
- Special Characters

. The program will generate a random password based on your preferences.

Example
Here's an example of generating a 12-character password with all character types included:

Enter password length: 12
Include uppercase letters (y/n): y
Include lowercase letters (y/n): y
Include digits (y/n): y
Include special characters (y/n): y

Generated Password: Ab#7zL!tE&vX
Custom Functions
Password generator's functionality is organized into several custom functions to provide a structured and modular codebase:

generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True): Generates a random password with specified length and character type options.

get_password_options(use_uppercase, use_lowercase, use_digits, use_special_chars): Returns a tuple of password generation options.

get_password_length(length): Validates and returns the password length as an integer.

generate_password_with_options(length, use_uppercase, use_lowercase, use_digits, use_special_chars): Generates a password using specified options.

Test Suite (test_project.py)
Ensuring the reliability and correctness of Pgen's functionality is paramount. The test_project.py file contains a comprehensive suite of pytest tests. These tests cover various scenarios, evaluating the password generation and validation functions to ensure they work flawlessly.

Whether it's generating a strong password for a new online account or enhancing the security of existing ones, Pgen is a valuable tool that empowers users to take control of their online safety.
