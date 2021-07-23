import random
import string



#This is the length of the password required

MAX_LEN = 8

#The character set from which random characters are going to be chosen from

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

#combining all the characters

all = 2*lower + 2*upper + 2*number + symbols

#For the program to randomly choice characters

gen = random.sample(all, MAX_LEN)

#Creating the password

password = "".join(gen)

print(password)