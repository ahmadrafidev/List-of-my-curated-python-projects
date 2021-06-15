from array import array
from math import comb
import random
import array
import string


digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

    
combine = digit + lowerCase + upperCase + symbols

randomDigit = random.choice(digit)
randomLower = random.choice(lowerCase)
randomUpper = random.choice(upperCase)
randomSymbols = random.choice(symbols)


password = randomDigit + randomLower + randomUpper + randomSymbols

for i in range(12):
    password += random.choice(combine)
    tempPass = array.array('u', password)
    random.shuffle(tempPass)

passWord = ""
for i in tempPass:
    passWord += i

    
print(passWord)