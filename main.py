import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters= int(input("How many letters would you like in your password?\n")) 
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

# Easy Level - Order not randomized:
#e.g. 4 letter, 2 number, 2 symbol = JduE91&!

password = []

for n in range(0, num_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])

for n in range(0, num_numbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

for n in range(0, num_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])

# password = ''.join(password_list)
# print(password)

# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 number, 2 symbol = g^2jk8&P

random.shuffle(password)
password = ''.join(password)
print(password)
