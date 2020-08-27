print('This is python scripting')
print('create new string')
print('creating new string 2')
print('delete new string 2')
print('use new string')

#variables
print('learning variables')

application = 'learning'
print(application + ' variables_1')

message = application + ' variables_2'
print(message)

message = application + ' python variables'
python_message = message
print(python_message)

variables = ' python3 variables!!'

message = application + variables

python_message = message

print(python_message)

#Datatypes and Typecasting
print(type(1))
print(type('cyberman'))
print(type(True))

#changing types
a = float(1)#1.0

b = int('1')#1

c = int(float('2.3'))#2

d = str(int('4'))#'4'

e = int(float(3))#3

f = str(int(float(3)))#'3'

types_array = [a, b, c, d, e, f]
print(types_array)

#variables and datatypes excercise.#

#print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

windows_laptop = float(700)
apple_laptop = float(1000)

in_stock = True
no_stock = False

message = 'The windows laptop cost $' + str(windows_laptop) + '0. in-stock: ' + str(in_stock)
windows_msg = message
print(windows_msg)

message_1 = 'The apple laptop cost $' + str(apple_laptop) + '0. in-stock: ' + str(no_stock)
apple_msg = message_1
print(apple_msg)

windows_count = 105
apple_count = 0

print(message + '. count: ' + str(windows_count))
print(message_1 + '. count: ' + str(apple_count))

item = 'windows x system update'
price = 99.00

item2 = 'macOs 13.1.6 system update'
price_1 = 'free'
instock = True
nostock = False

print(item, price, instock)
print(item2, price_1, nostock)

#basic arithmatic
new_skill = 'addition: '
a = 5
b = 3
print(new_skill, a + b)

new_skill = 'subtraction: '
print(new_skill, a - b)

new_skill = 'multiplication'
print(new_skill, a * b)

new_skill = 'division'
print(new_skill, a / b)

new_skill = 'division (floor)'
print(new_skill, a // b)#exact quotient

new_skill = 'modulus'
print(new_skill, a % b)

new_skill = 'exponent'
print(new_skill, a ** b)

#slicing
message = 'python\'s string'
print(message, message)#multiplying strings

print(message.upper())#all letters are cpitalized

print(message.lower())#all letters are lowercase

print(message.capitalize())#first letter is uppercase

print(message.title())#all first letters are uppercase










