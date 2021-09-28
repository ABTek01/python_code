#conditional statements and control flow

user_name = 'cyberman'

if user_name == 'cyberman':
   print('username is the primary user: ' + user_name)

if user_name == 'hacker1'
   print('system hacked')

#relational operators II

# > greater than

# >= greater then or equal to

# < less than

# <= less than or equal to

#exercise; check to see if student has enough credits to graduate.

credits = 160

if credits >= 160:
   print('you have enough credits to graduate')


#boolean operators/logical operators; and, or, not

# and; combines two boolean expressions and evaluates as True if both components are True, but False otherwise.
# oranges are a fruits and carrots are a vegetable. 

#excercise; check if a student has enough credits and if his gpa is above a 2.0

gpa = 3.4

if credits >= 120 and gpa >= 2.0:
   print('congrats graduate!!')  


# or; combines two expressions into a larger expressions that is True if either components is True.
#only one component needs to be True for an or stetement to be True.
# oranges are a fruits or apples are a vegetable.

#excercise; check if student has more than enough credits or has a gpa of 2.0 or above.

credits = 120
gpa = 1.9

if credits >= 120 or gpa >= 2.0:
   print('you have met at least one of the requirements')

# not; when applied to any boolean expression it reverses the boolean value.
# So if we have a True statement and apply a not operator we get a False statement.
# Oranges a not a fruit.

statement_one = not (2 * 2 == 5 - 1)

statement_two = not (7 * 7 == 49 > 0)

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")


#else statements; This prevents us from needing to write if statements for each possible condition,
#we can instead write a blanket else statement for all the times the condition is not met.

gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


#else if(elif);We can use elif statements to control the order we want our program to check each of our conditional statements.

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")


#
