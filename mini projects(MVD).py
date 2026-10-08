#-----mini project 1------(student profile card)
#take input from user:name,age,city,college
name = input("Enter your name :")
age = int(input("Enter your age :"))
city = input("Ente your city :")
college = input("Enter your college :")
print("------Student Profile------")
print("Name :",name)
print("Age :",age)
print("City :",city)
print("College :",college)
print(name[0])


#----- mini project 2------(simple calculator)
#take two numbers from user and print basic arithmatic operations
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
sum = num1 + num2 
substraction = num1 - num2 
multiplication = num1 * num2
division = num1 / num2 
print("Sum :",sum) 
print("Substraction :",substraction) 
print("Multiplication :",multiplication) 
print("Division :",division) 


#------mini project 3------(Lucky number generator)
#take user name use module and print lucky number
name = input("Enter your name :") 
print("Welcome" ,name) 
import random 
lucky = random.randint(1,10) 
print("Your Lucky Number is",lucky) 
print("Have a nice day!") 