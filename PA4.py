# assignment: programming assignment 4
# author: Muzzammil Adamjee
# date: November 19th 2021
# file: cipher.py is a program that takes user input for a text file, then user input for either decoding or 
# encoding that file using a 3 shift ceaser cipher. It also takes user input for another file in which either
# the encoded or decoded message is written to.
# input: user string input of file names within the directory
# output: console output of the encoding and decoding operations, and also a user-chosen file which contains
# the encoded or decoded message.


def readfile():
    file = input("enter a file for reading: ")
    try:
        with open(f"{file}") as file_:
            message = ''
            for i in file_:
                for char in i:
                    message += char
            return message
    except FileNotFoundError:
        print("that file doesnt exist")
        return None
    



def writefile(message):
    file = input("enter a file for writing: ")
    try:
        with open(f"{file}", "w") as f2:
            f2.write(message)
            return message
    except FileNotFoundError:
        print("that file doesnt exist")
        return None
   
        
        

def make_alphabet():
    alphabet = ()
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    return alphabet


def encode(plaintext):
    plaintext = plaintext.upper()
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    for char in plaintext:
        found = False
        for i in range(26):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % 26]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return ciphertext


def decode(ciphertext):
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    for char in ciphertext:
        found = False
        for i in range(26):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % 26]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext


def to_string(text):
    s = ""
    for i in text:
        s += i
        
    return s


# main program
operating = True
while operating:
    user_choice = input("would you like to encode or decode your message?\nType D to decode, E to encode, or Q to quit: ")

    if user_choice == "E" or user_choice == "e":
        ms = readfile()
        try:
            tx = to_string(encode(ms))
        except:
            break
        writefile(tx)
        print(f"Plaintext:\n{ms}\nCiphertext:\n{tx}")
        operating = True
    
    elif user_choice == "D" or user_choice == "d":
        ms = readfile()
        try:
            tx = to_string(decode(ms))
        except:
            break
        writefile(tx)
        print(f"Ciphertext:\n{ms}\nPlaintext:\n{tx}")
        operating = True

    
    elif user_choice == "Q" or user_choice == "q":
        print("Goodbye!")
        operating = False
