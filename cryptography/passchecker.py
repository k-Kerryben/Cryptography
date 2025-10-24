# Password Strength Checker (with entropy analysis)

import re
import math
import getpass

def calculate_entropy(password):
    """Calculate theoretical password entropy based on character set size."""
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32

    if charset == 0:
        return 0  # avoid math domain error if password is empty or invalid
   
    # check for the entropy of the password
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def pass_check(password):
    
    score = 0
    feedback = []

    # Basic rules
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Common pattern detection
    common_patterns = [
        r'(.)\1{2,}',
        r'(123|234|345|456|567|678|789|890)',
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
        r'(qwerty|asdfgh|zxcvbn)',
        r'(password|letmein|welcome|admin|user|login)',
    ]
    pattern_found = any(re.search(p, password, re.IGNORECASE) for p in common_patterns)
    if pattern_found:
        feedback.append("Your password contains common patterns or sequences.")
    else:
        score += 1

    # Entropy calculation
    entropy = calculate_entropy(password)
    # if entropy < 28:
    #     strength = 
    # elif entropy < 36:
    #     strength = 
    # else:
    #     strength = 

    # Combine both metrics (optional)
    # For a more accurate overall rating, we can balance score + entropy:
    if score <= 3 and entropy < 28:
        strength = "Weak password, consider increasing complexity."
    elif score >= 5 and 28 <= entropy < 36:
        strength = "Medium, you can do better!"
    elif score >= 6 and entropy >= 36:
        strength = "Strong, good job!" 

    return strength, feedback, entropy
def main():
    passwd = getpass.getpass("Enter password: ")
    strength, feedback, entropy = pass_check(passwd)

    print(f"\nPassword Strength: {strength}")
    print(f"Entropy: {entropy} bits")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")


if __name__ == "__main__":
    main()