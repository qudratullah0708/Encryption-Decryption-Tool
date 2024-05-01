import string
import random

def reverse_string(s):
    return ''.join(reversed(s))

def rand_generator(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def encrypt(user_input):
    words = user_input.split(" ")
    encrypted_string = []
    for word in words:
        rand = rand_generator(3)
        word = rand + word[1:] + word[0] + rand
        encrypted_string.append(word)
    print("Encrypted string:" ," ".join(encrypted_string))
    print("*************")
    
def decrypt(user_input):
    words = user_input.split(" ")
    decrypted_string = []
    for word in words:
        if len(word) < 3:
            decrypted_string.append(reverse_string(word))
        else:
            word = word[3:-3]
            word = word[-1] + word[:-1]
            decrypted_string.append(word)
    print("Decrypted string:" ," ".join(decrypted_string))
    print("*************")
    
while True:
    print("What do you want to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        user_input = input("Enter the string to encrypt: ")
        encrypt(user_input)
    elif choice == 2:
        user_input = input("Enter the string to decrypt: ")
        decrypt(user_input)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
