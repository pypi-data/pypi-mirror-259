#! /usr/bin env python3

#import string module for getting alphebet
import string

def formula(letter):
    key = 3 #key value of the encryption
    if letter.islower():
        #lowercase letter encryption
        return(chr((ord(letter) + key - 97) % 26 + 97))
    else:
        #uppercase letter encryption
        return (chr((ord(letter) + key - 65) % 26 + 65))

if __name__ == '__main__':
    #getting lowercase letters
    lowercase_letters = list(string.ascii_lowercase)

    #getting uppercase letters
    uppercase_letters = list(string.ascii_uppercase)

    #get ascii value of lowercase letters
    for i in range(26):
        print(f"{lowercase_letters[i]} after apply formula value is : -\t"+str(formula(lowercase_letters[i])))

    #add 2 line brakes
    print("\n\n")

    #get ascii value of uppercase letters
    for i in range(26):
        print(f"{uppercase_letters[i]} after apply formula value is : -\t"+str(formula(uppercase_letters[i])))