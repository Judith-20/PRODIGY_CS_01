letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():  # Check if the character is a letter
            is_upper = letter.isupper()  # Check if it's uppercase
            letter = letter.lower()  # Convert to lowercase for processing
            index = letters.find(letter)
            new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters
            new_letter = letters[new_index]
            if is_upper:  # Convert back to uppercase if needed
                new_letter = new_letter.upper()
            ciphertext += new_letter
        else:
            ciphertext += letter  # Keep spaces and non-letters as they are

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():  # Check if the character is a letter
            is_upper = letter.isupper()  # Check if it's uppercase
            letter = letter.lower()  # Convert to lowercase for processing
            index = letters.find(letter)
            new_index = index - key
            if new_index < 0:
                new_index += num_letters
            new_letter = letters[new_index]
            if is_upper:  # Convert back to uppercase if needed
                new_letter = new_letter.upper()
            plaintext += new_letter
        else:
            plaintext += letter  # Keep spaces and non-letters as they are

    return plaintext

print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

while True:
    user_input = input("Do you want to encrypt or decrypt (e/d)? ").lower()
    if user_input in ["e", "d"]:
        break
    else:
        print("Invalid input! Please enter 'e' for encryption or 'd' for decryption.")
        print()

print()

if user_input == "e":
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == "d":
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
    
    
    # letters = "abcdefghijklmnopqrstuvwxyz"
# num_letters = len(letters)

# def encrypt(plaintext, key):
#     ciphertext = ""
#     for letter in plaintext:
#         letter = letter.lower()
#         if letter != " ":
#             index = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 ciphertext += letters[new_index]
#         else:
#             ciphertext += letter  # Keep spaces as is

#     return ciphertext


# def decrypt(ciphertext, key):
#     plaintext = ""
#     for letter in ciphertext:
#         letter = letter.lower()
#         if letter != " ":
#             index = letters.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index = index - key
#                 if new_index < 0:
#                     new_index += num_letters
#                 plaintext += letters[new_index]
#         else:
#             plaintext += letter  # Keep spaces as is

#     return plaintext


# print()
# print("*** CAESAR CIPHER PROGRAM ***")
# print()

# # print("Do you want to encrypt or decrypt?")

# # user_input = input("e/d: ").lower()
# # print()

# while True:
#     user_input = input("Do you want to encrypt or decrypt (e/d)? ").lower()
#     if user_input in ["e", "d"]:
#         break
#     else:
#         print("Invalid input! Please enter 'e' for encryption or 'd' for decryption.")
#         print()

# print()

# if user_input == "e":
#     print("ENCRYPTION MODE SELECTED")
#     print()
#     key = int(input("Enter the key (1 through 26): "))
#     text = input("Enter the text to encrypt: ")
#     ciphertext = encrypt(text, key)
#     print(f'CIPHERTEXT: {ciphertext}')

# elif user_input == "d":
#     print("DECRYPTION MODE SELECTED")
#     print()
#     key = int(input("Enter the key (1 through 26): "))
#     text = input("Enter the text to decrypt: ")
#     plaintext = decrypt(text, key)
#     print(f'PLAINTEXT: {plaintext}')

