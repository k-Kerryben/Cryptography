import re
import getpass

def pass_check(password):
    #create a score line that we can use to evaluate the strength of the password
    score = 0
    #create a list the we can add the feedbacks into
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
     # Check for common patterns   
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
    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"   
    return strength, feedback

# cature password input securely using the getpass module
def main():
    passwd = getpass.getpass("Enter password: ")
    strength, feedback = pass_check(passwd)
    print("Strength:", strength)
    if feedback:
        print("Feedback:")
        for f in feedback:
            print("-", f)
# Run the main function to start the program
if __name__ == "__main__":
    main()
    
    #I've never done something this impressive before.
    #I feel accomplished and proud of my work.
    #try adding it to a GUI next?