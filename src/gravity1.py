'''
Created on Oct. 11, 2023
Caeser Cipher decoder
@author: Sebastian
'''

def decrypt_caesar(text, shift): #decrypt a shift of any length
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #easier than typing out each comma and quotation marks
    lower = list("abcdefghijklmnopqrstuvwxyz")
    converted = []
    
    for char in text :
        if char.isupper(): #checks to see if it needs to use the uppercase letters
            encrypted_idx = upper.index(char) #finds the index of the uppercase encrypted letter
            decrypted = upper[encrypted_idx-shift] #finds the corresponding decrypted letter
            converted.append(decrypted) #adds converted letter
        elif char.islower(): #checks to see if it needs to use the lowercase letters
            encrypted_idx = lower.index(char)
            decrypted = lower[encrypted_idx-shift]
            converted.append(decrypted) #adds converted letter
        else :
            converted.append(char) #for all non alphabet characters simply add them to the list
    print("".join(converted)) #combines the list and an empty string making the list a string

def main() :
    text = input("Enter a text to decypher: ") 
    decrypt_caesar(text, 3)
    
main()
