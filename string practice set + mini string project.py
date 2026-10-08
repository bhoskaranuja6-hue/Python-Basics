#write a python program to display a user entered name followed by goof afternoon using input()function
name = input('Enter your name :')
print(f"Good Afternoon , {name}")

#write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Anuja").replace("<|Date|>","28 september 2026"))

#write a program to detect double space in a string
name = "Anuja is a good  girl"
print(name.find("  "))

#replace the double space in 3 problem with single space
name = "Anuja is a good  girl"
print(name.replace("  "," "))

#write a program to format the following letter using escape sequence chracters
#letter = "Dear Anuja, this python course is nice. Thanks!"
letter = "Dear Anuja,\n\tThis python course is nice.\n Thanks!"
print(letter)

#-----mini project 1------(string Information project)
#input:enter a sentence and output:original,uppercase,lowercase,title case,length,reversed
sentence = input("Enter a sentence :")
uppercase = sentence.upper()
lowercase = sentence.lower()
title = sentence.title()
lenght = len(sentence)
reversed = sentence[::-1]
print("Original :",sentence)
print("Uppercase :",uppercase)
print("Lowercase :",lowercase)
print("Title Case :",title)
print("Length :",lenght)
print("Reversed :",reversed)

#-----mini project 2(name formatter)-----
name = input("Enter your full name :")
no_espace = name.strip()
uppercase = name.upper()
lowercase = name.lower()
title = name.title()
capitalized = name.capitalize()
lenght = len(name)

print("No Space :",no_espace) 
print("Uppercase :",uppercase) 
print("Lowercase :",lowercase) 
print("Title Case :",title) 

