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