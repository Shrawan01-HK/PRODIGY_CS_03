# Password-Complexity-Checker
# Password Strength Assessor

This repository contains a Python application that assesses the strength of passwords using a graphical user interface (GUI) built with Tkinter. The tool evaluates user-entered passwords based on length and complexity criteria, providing feedback on their strength.

## Overview

The Password Strength Assessor allows users to input a password and receive instant feedback on its strength. It checks for various criteria, including length, presence of uppercase and lowercase letters, numbers, and special characters.

### Key Features

- **User-Friendly Interface**: A simple GUI enables users to easily enter and assess their passwords.
- **Strength Assessment**: The application evaluates passwords based on:
  - Minimum length of 8 characters.
  - Inclusion of uppercase letters, lowercase letters, numbers, and special characters.
- **Feedback Mechanism**: Users receive detailed feedback on password strength, categorized as weak, medium, or strong.

## How It Works

1. **Input Field**: Users can enter their password into a secure input field that masks their input.
2. **Assessment Button**: By clicking the "Assess Password Strength" button, the application evaluates the entered password.
3. **Feedback Display**: The result of the assessment is displayed on the GUI, providing users with insights into their password's strength.

### Criteria for Password Strength

- **Length**: Passwords must be at least 8 characters long.
- **Character Diversity**: Passwords should contain:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character (e.g., !@#$%^&*)

## Example Usage

1. Launch the application.
2. Enter a password in the provided field.
3. Click on the "Assess Password Strength" button.
4. Review the feedback on password strength.

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)

## License

This project is open-source and licensed under the MIT License. Contributions and improvements are encouraged!
