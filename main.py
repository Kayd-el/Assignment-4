import random

print("Welcome to the random password generator")
name = input("Enter any word: ")
while True:
    a = int(input("Now enter a series of 8 numbers: "))
    if len(str(a)) == 8:
        break
    else:
        print("The option you entered was not valid, please try again.")

b = list(str(a))
random.shuffle(b)
randomized = ""

i = 0
while i < 8:
    randomized += str(b[i])
    i += 1
password = name + randomized
print("Your new password is: %s" % password)


