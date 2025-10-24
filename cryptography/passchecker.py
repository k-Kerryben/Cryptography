#Password Strength Checker

import re #regular expressions for pattern matching
import getpass #secure password input

def pass_check(password):
    #create a score line that we can use to evaluate the strength of the password
    score = 0
    #create a list the we can add the feedbacks into
    feedback = []

    if len(password) >= 8:
        score += 1  
    else:
        feedback.append("Password should be at least 8 characters long.")
        #check for digits
    if re.search(r"\d", password):
        score += 1 
    else:
        feedback.append("A password should include at least one digit.")
    if re.search(r"[A-Z]", password):
        score += 1  
    else:
        feedback.append("A password should include at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("A password should include at least one lowercase letter.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1  
    else:
        feedback.append("A password should include at least one special character.")
    
     # Check for common patterns   
    common_patterns = [
        #abc #aaaa
        r'(.)\1{2,}', #three or more repeated characters
        r'(123|234|345|456|567|678|789|890)',
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
        r'(qwerty|asdfgh|zxcvbn)',
        r'(password|letmein|welcome|admin|user|login)',
    ]
    # searching for any pattern in the password ingoring the case (e.g RrRr) if it matches any pattern in the common_patterns list
    pattern_found = any(re.search(pattern, password, re.IGNORECASE)  for pattern in common_patterns)
    if pattern_found:
        feedback.append("Your password contains common patterns or sequences.")
    else:
        score += 1  
    # Determine strength based on score
    if score == 6:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"   
    return strength, feedback

# cature password input securely using the getpass module
def main():
    # passwd = input("Enter password: ")---->> this wouldn't be a safe way to capture passwords
    passwd = getpass.getpass("Enter password: ")
    # here we're initialising two variables at the same time because we want to call a single function
    # you can initialise them individually and call the function twice but we are trying to reduce redundancy
    strength, feedback = pass_check(passwd)
    
    print("Your password is ", strength)
    if feedback:
        print("What you should know:")
        for f in feedback:
            print("-", f)
# Run the main function to start the program
if __name__ == "__main__":
    main()
    
    #It's been a while since I wrote some serious code.
    #I feel accomplished and proud of my work.
    #try adding it to a GUI next?