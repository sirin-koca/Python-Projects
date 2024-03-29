# If-statements and Boolean expressions:

# ex0
is_hot = False
is_cold = True
if is_hot:
    print("Drink water")
elif is_cold:
    print("Wear warm clothes")
else:
    print("Its a lovely day!")


# ex1
test_value = 100

if test_value > 1:
    print("This code is executed!")

if test_value > 1000:
    print("This code is NOT executed!")

print("Program continues at this point.")
print("*" * 10)

# ex2
pet = "dog"

if pet == "dog":
    print("You have a dog!")
elif pet == "cat":
    print("You have a cat!")
elif pet == "fish":
    print("You have a fish!")
else:
    print("You dont have a pet!")

name = input("Whats the name of your dog?")
print("My dogs name is " + name)
print("*" * 10)

# ex3
uname = input("Hello, what is your name?")
if uname == "Dave":
    print("Get off my computer Dave!")
    print("*" * 10)

is_raining = True
if is_raining:
    print("It is going to rain today. Bring an umbrella! ")
    print("*" * 10)

age = 12
if age <= 13:
    print("You are underage, and parental control required")
    print("*" * 10)

# *** AND / OR ***
student_credits = 118
gpa = 2.0
if student_credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")
    print("*" * 10)

if pet == "dog" and name == "Maya":
    print("I love you, Maya!")

# *** IF NOT ***
s_credits = 120
gpa = 1.8

if not s_credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not s_credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")

# ELIF:
# Remember to cast user-input if you are dealing with numbers:
donation = int(input("How much you would like to donate?"))
print("Thank you for the donation!")

if donation >= 1000:
    print("You've achieved platinum status")
elif donation >= 500:
    print("You've achieved gold donor status")
elif donation >= 100:
    print("You've achieved silver donor status")
else:
    print("You've achieved bronze donor status")

# ex
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

# ex
x = 5

if x <= 2:
    print("This is printed")
if x <= 4:
    print("This is also printed")
if x <= 6:
    print("Is this printed?")
if x <= 8:
    print("This might be printed.")

# ex
x = 0

if x == 0:
    print("x is equal to zero")
elif x >= 0:
    print("x is greater than zero")
else:
    print("x is less than zero")

"""The line "if x = 0:" will cause a SyntaxError because = is not a relational operator. If this was fixed, 
then x is equal to zero would print, but “x is greater than zero” would not print because the elif conditional would 
not be checked."""


exit()
