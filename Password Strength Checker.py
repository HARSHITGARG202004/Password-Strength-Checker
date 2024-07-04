import re

def password_strength_checker(password):
    # Criteria for checking password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count how many criteria are met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Output the strength and detailed criteria results
    return {
        "strength": strength,
        "criteria": {
            "length_criteria": length_criteria,
            "lowercase_criteria": lowercase_criteria,
            "uppercase_criteria": uppercase_criteria,
            "digit_criteria": digit_criteria,
            "special_char_criteria": special_char_criteria
        }
    }

# Example usage
password = input("Enter a password to check its strength: ")
result = password_strength_checker(password)
print(f"Password Strength: {result['strength']}")
print("Criteria Met:")
print(f" - Length Criteria (>= 8 characters): {'Yes' if result['criteria']['length_criteria'] else 'No'}")
print(f" - Lowercase Letter: {'Yes' if result['criteria']['lowercase_criteria'] else 'No'}")
print(f" - Uppercase Letter: {'Yes' if result['criteria']['uppercase_criteria'] else 'No'}")
print(f" - Digit: {'Yes' if result['criteria']['digit_criteria'] else 'No'}")
print(f" - Special Character (@$!%*?&): {'Yes' if result['criteria']['special_char_criteria'] else 'No'}")
