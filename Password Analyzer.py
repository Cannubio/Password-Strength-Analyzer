import re
import random
import string
import math

# Common password database (you can expand this list)
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "abc123", "test", "12qwaszx!@QWASZX",
    "12345678", "iloveyou", "admin", "welcome", "monkey", "letmein", "football", "shadow",
    "master", "dragon", "sunshine", "password1", "123123", "654321", "superman", "trustno1"
]

# Function to calculate entropy
def calculate_entropy(password):
    unique_chars = len(set(password))
    length = len(password)
    return length * math.log2(unique_chars) if unique_chars > 0 else 0

# Function to calculate password score
def calculate_password_score(password):
    score = 0
    max_score = 100

    # Length check (20 points)
    if len(password) >= 12:
        score += 20
    elif len(password) >= 8:
        score += 10

    # Character variety checks (20 points each)
    if any(c.isupper() for c in password):
        score += 20
    if any(c.islower() for c in password):
        score += 20
    if any(c.isdigit() for c in password):
        score += 20
    if any(c in string.punctuation for c in password):
        score += 20

    # Entropy contribution (up to 20 points)
    entropy = calculate_entropy(password)
    if entropy >= 60:
        score += 20
    elif entropy >= 40:
        score += 10

    # Cap the score at the maximum
    return min(score, max_score)

# Function to analyze password strength
def analyze_password(password):
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Increase password length to at least 12 characters.")

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Add at least one uppercase letter (e.g., A, B, C).")

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Add at least one lowercase letter (e.g., a, b, c).")

    # Check for digits
    if not re.search(r'\d', password):
        feedback.append("Add at least one number (e.g., 1, 2, 3).")

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Include at least one special character (e.g., !, @, #, $).")

    # Check against common password database
    if password in COMMON_PASSWORDS:
        feedback.append("Avoid using common passwords like '123456' or 'password'.")

    # Calculate entropy (only used internally for randomness checks)
    entropy = calculate_entropy(password)
    if entropy < 60:
        feedback.append("Increase password randomness.")

    # Strength classification
    score = calculate_password_score(password)
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, feedback

# Function to generate a secure password
def generate_secure_password(length=16):
    if length < 12:
        print("Warning: Password length is less than 12. Setting to minimum length of 12.")
        length = 12  # Enforce minimum length of 12

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main execution
def main():
    print("Welcome to my project for security automation\n")
    print("Password Strength Analyzer")
    print("---------------------------")

    while True:
        # User enters their password
        password = input("Enter your password: ")
        
        # Analyze password
        strength, score, feedback = analyze_password(password)
        print(f"\nPassword Strength: {strength}")
        print(f"Password Score: {score}%")
        if feedback:
            print("Feedback:")
            for suggestion in feedback:
                print(f"- {suggestion}")

        if score == 100:
            print("Thank you for participating in my final project!")
            break  # Exit if the password is perfect
        else:
            print("Your password does not meet the 100% strength requirement. Please follow the feedback and try again.")
            print("\nRecommended Requirements:")
            print("- Minimum length: 12 characters")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one number")
            print("- At least one special character")

    # No secure password generation for now
    # Removed the exit message for secure password generation

if __name__ == "__main__":
    main()