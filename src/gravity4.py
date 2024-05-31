'''
Created on Oct. 11, 2023
Combining multiple types of decryption
@author: Sebastian
'''

UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #easier than typing out each comma and quotation marks
LOWER = list("abcdefghijklmnopqrstuvwxyz")

def decrypt_caesar(text, shift): #decrypt a shift of any length
    converted = []
    
    for char in text :
        if char.isupper(): #checks to see if it needs to use the uppercase letters
            encrypted_idx = UPPER.index(char) #finds the index of the uppercase encrypted letter
            decrypted = UPPER[encrypted_idx-shift] #finds the corresponding decrypted letter
            converted.append(decrypted) #adds converted letter
        elif char.islower(): #checks to see if it needs to use the lowercase letters
            encrypted_idx = LOWER.index(char)
            decrypted = LOWER[encrypted_idx-shift]
            converted.append(decrypted) #adds converted letter
        else :
            converted.append(char) #for all non alphabet characters simply add them to the list
    return("".join(converted)) #combines the list and a string specifying what type of cipher making the list a string

def decrypt_atbash(text):
    converted = []
    
    for char in text :
        if char.isupper(): #checks to see if it needs to use the uppercase letters
            encrypted_idx = UPPER.index(char) #finds the index of the uppercase encrypted letter
            decrypted = UPPER[25-encrypted_idx] #finds the corresponding decrypted letter, I use 15 instead of 26 to account for the last index being 25 due to it starting at 0
            converted.append(decrypted) #adds converted letter
        elif char.islower(): #checks to see if it needs to use the lowercase letters
            encrypted_idx = LOWER.index(char)
            decrypted = LOWER[25-encrypted_idx]
            converted.append(decrypted) #adds converted letter
        else :
            converted.append(char) #for all non alphabet characters simply add them to the list
    return("".join(converted)) #combines the list and a string specifying what type of cipher making the list a string

def decrypt_a1z26(text): 
    for value in range(26,0,-1) : #counts down from 26 to 1 (corresponds to letters of the alphabet), counts down because of the double digit letters
        text = text.replace(str(value), UPPER[value -1])
    
    text = text.replace("-", "") #removes all the hyphens
    return(text)
    
def main() :
    text = input("Enter a text to decypher: ") 
    print("Let's try all the methods we have:")
    print("Caesar Cipher: " + decrypt_caesar(text, 3)) #1
    print("Atbash Cipher: " + decrypt_atbash(text)) #2
    print("Combined: 1) Atbash; 2) Caesar cipher: " + decrypt_caesar(decrypt_atbash(text),3))
    print("A1Z26 Cipher: " + decrypt_a1z26(text)) #5
    print("Combined: 1) A1Z26; 2) Caesar cipher: " + decrypt_caesar(decrypt_a1z26(text),3)) #6
    print("Combined: 1) A1Z26; 2) Atbash cipher: " + decrypt_atbash(decrypt_a1z26(text))) #7
    print("Combined: 1) A1Z26; 2) Atbash 3) Caesar cipher: " + decrypt_caesar(decrypt_atbash(decrypt_a1z26(text)),3))
    print("Combined: 1) A1Z26; 2) Caesar 3) Atbash cipher: " + decrypt_atbash(decrypt_caesar(decrypt_a1z26(text),3)))
    
main()