#Varible
#create a varible name and store your name to it.print it
name = "Anuja"
print(name)

#create varible age and city print(I am 18 years old and I live in nagpur)
age = 18
city = "Nagpur"
print("I am",age,"year old and I live in",city)

#store two number in varible and print their sum
num1 = 3
num2 = 5
sum = num1 + num2
print(sum)


#Datatype
#for each varible identify the datatype using type()
int = 10
print(type(int))
float = 3.14
print(type(float))
a = "Hello"
print(type(a))
is_student = True
print(type(is_student))


#string
#store"Python" in varible an print it 
a = "Python "
print(a)

#print first letter pf "Python"
word = "Python"
print(word[0])

#add two strings
name1 = "Anuja"
name2 = "Bhoskar"
print(name1, name2)


#Number practice 
#add 25 and 10
num1 = 25
num2 = 10
print(num1 + num2)

#substract 50 from 100
num1 = 100
num2 = 50
print(num1 - num2)

#multipy 7 and 8
num1 = 7
num2 = 8
print(num1 * num2)

#Divide 20 by 8
num1 = 20
num2 = 8
print(num1 / num2)


#User Input
name = input("Enter your name :")
print("welcome",name)

#create varible for name,age,college and print all together
name = "Anuja"
age = 18
college = "JIT Nagpur"
print(name + str(age)+ college)
print(name , age , college)

a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#swap two numbers
x = 10
y = 50
temp = x
x = y
y = temp
print(x)
print(y)

#Modules
#import the math module and find sq root of 25
import math
print(math.sqrt(25))
print(math.isqrt(25))

#use random module to print a random number from 1 to 10
import random
print(random.randint(1 , 10))

#make a simple student profile program
name = input("Enter your name :")
age = int(input("Enter your age :"))
city = input("Enter your city :")
college = input("Enter your college :")
print("--\nStudent Detail--")
print("Name :",name)
print("Age :",age)
print("City :",city)
print("College :",college)




