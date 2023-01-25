import random 
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","+","-","(",")"]
print("Welcome to the Password Generator...")
<<<<<<< HEAD
no_letters = int(input("How many Letters would you like in your Password?\n"))
no_numbers = int(input("How many Numbers would you like in your Password?\n"))
no_symbols = int(input("How many Symbols would you like in your Password?\n"))
=======
no_letters = int(input("How many letters would you like in your Password?\n"))
no_numbers = int(input("How many numbers would you like in your Password?\n"))
no_symbols = int(input("How many symbols would you like in your Password?\n"))
>>>>>>> e50fbb8eb2d589d05053f4817400e471f1eec67b


# password = ""
# for char in range(1,no_letters+1):
#     password = password+random.choice(letters)
# for char in range(1,no_numbers+1):
#     password = password+random.choice(numbers)
# for char in range(1,no_symbols+1):
#     password = password+random.choice(symbols)
# print(password) 

# password_1 =[]
# for char in range(1,no_letters+1):
#     password_1.append(random.choice(letters))
# for char in range(1,no_numbers+1):
#     password_list += random.choice(numbers)
# for char in range(1,no_symbols+1):
#     password_list += random.choice(symbols)
# print(password_1)
# random.shuffle(password_1)
# print(password_1)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")

password_list = []

for char in range(1, no_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, no_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, no_numbers + 1):
  password_list += random.choice(numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

<<<<<<< HEAD
print(f"Your Password 🙄: {password}")
=======
<<<<<<< HEAD
print(f"Your Password 😓: {password}")
=======
print(f"Your Password 🙄: {password}")
>>>>>>> Test2
>>>>>>> e50fbb8eb2d589d05053f4817400e471f1eec67b
