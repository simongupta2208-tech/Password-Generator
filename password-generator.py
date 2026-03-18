import random
import string

print("****Password Generator****")
length=int(input("enter password length"))
a=string.ascii_letters
b=string.digits
c=string.punctuation
z = a + b + c
password =""
for i in range(length):
    password += random.choice(z)
print("Generated Password",password)
