#take a string and print its length
name = input("Enter your name :")
print(len(name))

#take a string and print it
text = input("what is your name ?")
print(text)

#find a length of a string using len()
string = "Anuja"
print(len(string))

#print the first character of string
text = "Python is very easy"
print(text[0])

#print the last charcter of string
text = "Python is very easy"
print(text[-1])

#print first 3 charcter using slicing
text = "Python is very easy"
print(text[0:3])

#print last 3 charcter using slicing
text = "Python is very easy"
print(text[-3:])      # means print(text[-3:len(text)])

#reverse a string using slicing
text = "Python is very easy"
print(text[::-1])     #text[start : end : step(-1 means one step back)]

#convert string to uppercase
text = "Python is very easy"
print(text.upper())

#convert string to lowercase
text = "Python is very easy"
print(text.lower())

#capitalize 1st letter of string
name = "anuja"
print(name.capitalize())

# replace one word/one character with another
my_name = "gauri"
print(my_name.replace("gauri","Anuja"))

# remove space from beginning and end using strip()
text = " Anuja is python developer "
print(text.strip())

#concatenate two string
first_name = "dishita"
second_name = "raut"
print(first_name + " " + second_name)

#repeat a string two times
a = "1234567"
print(a * 3)

#check index of charcter using find()
index = "shree radharaman"
print(index.find("r"))

#count occurance of word using count()
name = "shree radharaman"
print(name.count("r"))

#split a sentence into words using split()
hello = "anuja gauri dishita shree"
print(hello.split())

#join words using join()
words = ["I" ,"Love","python"] 
print(" ".join(words))
fruits = ["mango" ,"bannana","apple"]
print(','.join(fruits))

#check wheather string starts with words using startswith()
string = "Hello Good Afternoon!"
print(string.startswith("H"))

#check wheather string end with words using endswith()
string = "Hello Good Afternoon"
print(string.endswith("n"))