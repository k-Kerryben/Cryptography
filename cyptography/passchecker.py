import re
import getpass

def pass_check(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  
    else:
        feedback.append("Password should be at least 8 characters long.")
    if re.search(r"\d", password):
        score += 1 
    else:
        feedback.append("Password should include at least one digit.")
    if re.search(r"[A-Z]", password):
        score += 1  
    else:
        feedback.append("Password should include at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1  
    else:
        feedback.append("Password should include at least one special character.")
        
    common_patterns = [
        r'(.)\1{2,}',
        r'(123|234|345|456|567|678|789|890)',
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
        r'(qwerty|asdfgh|zxcvbn)',
        r'(password|letmein|welcome|admin|user|login)',
    ]

    pattern_found = any(re.search(pattern, password, re.IGNORECASE) 
    for pattern in common_patterns)
    if pattern_found:
        feedback.append("Password contains common patterns or sequences.")
    else:
        score += 1  
 
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"   
    return strength, feedback


def main():
    passwd = getpass.getpass("Enter password: ")
    strength, feedback = pass_check(passwd)
    print("Strength:", strength)
    if feedback:
        print("Feedback:")
        for f in feedback:
            print("-", f)

if __name__ == "__main__":
    main()