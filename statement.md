Problem Statement:

Write a python program with a user-defined function named caesar_en()
that encrypts the entered plaintext to Caesar Cipher depending on key
and another function named caesar_de() that converts cypher text to
plain text depending on key. Call the functions based on user choice.

Code:

print(\"Caesar Cipher Encrypter and Decrypter!\") def caesar_en():
newtext=\"\" for ch in text: if ch.isalpha():
shifted=(ord(ch)-ord(\'a\')+key)%26 newtext+=chr(ord(\'a\')+shifted)
elif ch== \" \": newtext+= \" \" elif ch.isdigit():
shifted=(ord(ch)-ord(\'0\')+key)%10 newtext+=chr(ord(\'0\')+shifted)
else: newtext+=ch print(newtext) def caesar_de(): newtext=\"\" for ch in
text: if ch.isalpha(): shifted=(ord(ch)-ord(\'a\')-key)%26
newtext+=chr(ord(\'a\')+shifted) elif ch== \" \": newtext+=\" \" elif
ch.isdigit(): shifted=(ord(ch)-ord(\'0\')-key)%10
newtext+=chr(ord(\'0\')+shifted) else: newtext+=ch print(newtext)
newtext=\"\" act=int(input(\"Do you want the text to be : \\n 1.
Encrypted \\n 2. Decrypted \\n\")) if act==1: text=input(\"Enter text to
be encrypted using Caesar Cipher: \") key=int(input(\"Enter key: \"))
text=text.lower() caesar_en() elif act==2: text=input(\"Enter text to be
decrypted using Caesar Cipher: \") key=int(input(\"Enter key: \"))
text=text.lower() caesar_de()

Scope of the Project:

Aims to make user-friendly and easy to manipulate encrypter and
decrypter of Caesar Cipher. It aims to include conversion of digits and
alphabets and preservation of spaces and punctuations.

Features:

• Conversion of plaintext to cipher using caesar_en() • Conversion of
cipher text to plaintext using caesar_de() • Conversion of digits and
alphabets • Preservation of spaces and punctuations • Use of ASCII-based
functions like ord() and chr() • Use of string concatenation
