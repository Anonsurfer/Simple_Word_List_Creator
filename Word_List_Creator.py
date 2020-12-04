# This simple script allows you to create a wordlist and automatically saves it as .txt 
# if the final value of wordlist is 100 - it will create the wordlist from 0,1,2,3,4.... so on to 100.
import os # Importing the Os Module
keys_ = open("keys.txt",'w') # Creating a new txt file
keys_range = int(input("Enter the final value of the wordlist: ")) # aking the user for the length
print("Creating Wordlist !")
print("Please wait....")
for x in range(0,keys_range + 1):
    keys_.write(str(x)) # Chainging x to string so we can write inside the file !
    keys_.write("\n") # \n - new line so, we won't get the values on the same line !
print("Done Creating the Wordlist !")
print("Your File Is Saved Right here: {}".format(os.getcwd()))
print("File Name = 'keys.txt'")
# Feel Free to change and use the code for your personal use ;-)
