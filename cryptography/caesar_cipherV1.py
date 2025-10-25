letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plain_text, shift):
    cipher_text = ''
    plain_text = plain_text.replace(" ", "")
    for char in plain_text:
        if str(char).isalpha(): # check if the character is a letter
            #char = char.lower() 
            if char.isupper():
                    base = ord('A')
                    new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                    base = ord('a')
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                    
            cipher_text += new_char        
        else:
            cipher_text += char # if the character is not a letter just add it to the cipher text
    return cipher_text    

                # index = letters.index(char) # get the index of the character
                # new_index = index + shift # shift the index by the shift amount
                # if new_index >= len(letters): # if the new index is greater than the length of letters wrap around
                #     new_index = new_index - len(letters) # wrap around
                # cipher_text += letters[new_index] # add the shifted character to the cipher text
        

# Decrypt function that takes in a cipher text and a shift amount
def decrypt(cipher_text, shift):
    plain_text = ''
    for char in cipher_text:
        if str(char).isalpha(): # check if the character is a letter
            if char.isupper():
                    base = ord('A')
                    new_char = chr((ord(char) - base - shift) % 26 + base)
            else:
                    base = ord('a')
                    new_char = chr((ord(char) - base - shift) % 26 + base)
                    
            plain_text += new_char
        else:
            plain_text += char # if the character is not a letter just add it to the plain text
            
    return plain_text
          
            #char = char.lower()
            # if char in letters: # if the character is in the letters find its index
            #     index = letters.index(char) # get the index of the character
            #     new_index = index - shift # shift the index back by the shift amount
            #     if new_index < 0: # if the new index is less than 0 wrap around
            #         new_index = len(letters) + new_index # wrap around
            #     plain_text += letters[new_index] # add the shifted character to the plain text
       

print("Caesar Cipher Encryption and Decryption")
print("=" * 40)
print("do you want to (e)ncrypt or (d)ecrypt? ")
choice = input("Enter e or d: ").lower()
if choice == 'e':
    print("Encryption Mode Selected")
    print("=" * 40)
    text = input("Enter the text you want to encrypt: ")
    shift = int(input("Enter the shift amount (1-25): "))
    cipher_text = encrypt(text, shift)
    print(f"Encrypted Text: {cipher_text}")
elif choice == 'd':
    print("Decryption Mode Selected")
    print("=" * 40)
    text = input("Enter the text you want to decrypt: ")
    shift = int(input("Enter the shift amount (1-25): "))
    plain_text = decrypt(text, shift)
    print(f"Decrypted Text: {plain_text}")
else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")


    #Hi my name is Kerry and this is my 1st program
        