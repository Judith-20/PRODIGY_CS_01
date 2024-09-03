from tkinter import *
from tkinter import simpledialog, messagebox

root = Tk()
root.geometry("500x350")
root.title("Caesar Cipher Encryption and Decryption")

# letters = "abcdefghijklmnopqrstuvwxyz"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"  # Include special characters and numbers
num_characters = len(characters)

# Function to encrypt the text
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char in characters:
            index = characters.find(char)
            new_index = (index + key) % num_characters
            ciphertext += characters[new_index]
        else:
            ciphertext += char  # Keep characters not in the list as they are

    return ciphertext


# Decrypting the text
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char in characters:
            index = characters.find(char)
            new_index = (index - key) % num_characters
            plaintext += characters[new_index]
        else:
            plaintext += char  # Keep characters not in the list as they are

    return plaintext


# User Input
def get_user_choice():
    return simpledialog.askstring("Input", "Do you want to encrypt or decrypt (e/d)?").lower()

def get_key():
    return simpledialog.askinteger("Input", "Enter the key (1 through 94):")

def get_text_to_process(action):
    title = "Encryption Mode Selected" if action == "encrypt" else "Decryption Mode Selected"
    return simpledialog.askstring(title, f"Enter the text to {action}:")

def main():
    user_input = get_user_choice()
    if user_input not in ["e", "d"]:
        messagebox.showerror("Error", "Invalid input! Please enter 'e' for encryption or 'd' for decryption.")
        return

    key = get_key()
    if not (1 <= key <= num_characters):
        messagebox.showerror("Error", "Key must be between 1 and 94.")
        return

    text = get_text_to_process("encrypt" if user_input == "e" else "decrypt")

    if user_input == "e":
        ciphertext = encrypt(text, key)
        messagebox.showinfo("Ciphertext", f'CIPHERTEXT: {ciphertext}')
        print(f'CIPHERTEXT: {ciphertext}')
    elif user_input == "d":
        plaintext = decrypt(text, key)
        messagebox.showinfo("Plaintext", f'PLAINTEXT: {plaintext}')
        print(f'PLAINTEXT: {plaintext}')
if __name__ == "__main__":
    main()
    root.mainloop()

