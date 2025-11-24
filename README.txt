Caesar Cipher 
Encryption and Decryption
Definition:
The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a certain number of positions (called the key).
For example, encryption with a key of 3:
* a - d
* b - e
* x - a
* 7 - 0 (for digits)
Decryption with a key of 2:
* u - s
* c - a
* 8 - 6
This program lets you both encrypt and decrypt text using this method.
Key Features:
* Encrypt plaintext
* Decrypt encrypted text
* Supports:
o alphabets (a–z)
o digits (0–9)
o spaces and punctuation
* User-friendly console menu
Implementation:
1. The user chooses whether to encrypt or decrypt.
2. Enter the text.
3. Enter the numeric key.
4. The program prints the result based on the Caesar Cipher formula.
Code:
print("Caesar Cipher Encrypter and Decrypter!")
def caesar_en():
    newtext=""
    for ch in text:
        if ch.isalpha():
            shifted=(ord(ch)-ord('a')+key)%26
            newtext+=chr(ord('a')+shifted)
        elif ch== " ":
            newtext+= " "
        elif ch.isdigit():
            shifted=(ord(ch)-ord('0')+key)%10
            newtext+=chr(ord('0')+shifted)
        else:
            newtext+=ch
    print(newtext)
def caesar_de():
    newtext=""
    for ch in text:
        if ch.isalpha():
            shifted=(ord(ch)-ord('a')-key)%26
            newtext+=chr(ord('a')+shifted)
        elif ch== " ":
            newtext+=" "
        elif ch.isdigit():
            shifted=(ord(ch)-ord('0')-key)%10
            newtext+=chr(ord('0')+shifted)
        else:
            newtext+=ch
    print(newtext)
newtext=""
act=int(input("Do you want the text to be : \n 1. Encrypted \n 2. Decrypted \n"))
if act==1:
    text=input("Enter text to be encrypted using Caesar Cipher: ")
    key=int(input("Enter key: "))
    text=text.lower()
    caesar_en()
elif act==2:
    text=input("Enter text to be decrypted using Caesar Cipher: ")
    key=int(input("Enter key: "))
    text=text.lower()
    caesar_de()

Example:
Sample Result (Encryption):
Input: shruti,18,gurwara
Key: 1
Encrypted Output: tisvuj,29,hvsxbsb
Sample Result (Decryption):
Input: tisvuj292
Key: 1
Decrypted Output: shruti181
Skills Used:
* Python programming
* Functions
* String manipulation
* ASCII values (ord() and chr())
* Modulo operator (%)
Conclusion
This project helped me understand how encryption works at a basic level and also improved my Python fundamentals.
In the future, I may add:
* support for uppercase letters
* automatic key detection
