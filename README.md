# Caesar Cipher Program

This is a simple Python program that implements the Caesar Cipher algorithm for encrypting and decrypting text. The program preserves the case (uppercase and lowercase) and spaces of the original text during both encryption and decryption.

## How It Works

The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, "A" becomes "B", "B" becomes "C", and so on. The same key is used for both encryption and decryption, but the direction of the shift is reversed for decryption.

## Features

- Encrypts and decrypts text using the Caesar Cipher algorithm.
- Preserves the original capitalization and spacing of the input text.
- Handles non-alphabetical characters (e.g., spaces, punctuation) by leaving them unchanged.

## Requirements

- Python 3.x

## Usage

1. Run the program.
2. Choose whether you want to encrypt or decrypt a message.
3. Enter a shift key (an integer between 1 and 26).
4. Enter the text you wish to encrypt or decrypt.
5. The program will display the encrypted or decrypted text.

## Example

### Encryption
- Enter the text to encrypt: Hello World 
- Enter the key (1 through 26): 3 
- CIPHERTEXT: Khoor Zruog

### Decryption
- Enter the text to decrypt: Khoor Zruog 
- Enter the key (1 through 26): 3 
- PLAINTEXT: Hello World


## How to Run

1. Ensure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/).
2. Save the script in a `.py` file (e.g., `caesar_cipher.py`).
3. Open your terminal or command prompt.
4. Navigate to the directory where you saved the file.
5. Run the program using the command: python caesar_cipher.py


## Contributing

Feel free to fork this repository, make your changes, and submit a pull request. Any contributions to improve this program are welcome!


