# Password Strength Checker

## Overview
This Python project is a simple password strength checker that evaluates the strength of a given password based on predefined criteria. The program checks for the presence of lowercase letters, uppercase letters, digits, special characters, and ensures the password meets a minimum length requirement. Based on these criteria, the password is classified into different strength categories ranging from "Very Weak" to "Very Strong".

## Features
- **Length Criteria**: Password must be at least 8 characters long.
- **Lowercase Letter**: Password must contain at least one lowercase letter.
- **Uppercase Letter**: Password must contain at least one uppercase letter.
- **Digit**: Password must contain at least one numeric digit.
- **Special Character**: Password must contain at least one special character (@, $, !, %, *, ?, &).

## Password Strength Classification
- **Very Strong**: All five criteria are met.
- **Strong**: Four criteria are met.
- **Moderate**: Three criteria are met.
- **Weak**: Two criteria are met.
- **Very Weak**: Less than two criteria are met.

## Usage
To use this password strength checker, simply run the script and enter a password when prompted. The program will then evaluate the password and provide a strength classification along with details about which criteria were met.

## Example
Enter a password to check its strength: ExamplePassword123!
Password Strength: Very Strong
Criteria Met:
 - Length Criteria (>= 8 characters): Yes
 - Lowercase Letter: Yes
 - Uppercase Letter: Yes
 - Digit: Yes
 - Special Character (@$!%*?&): Yes
