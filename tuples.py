#Create a tuple containing 5 integers
t1 = (1,2,3,4,5)
print(t1)

#find the length of a tuple
t = (4,5,6)
print(len(t))

#print the first element
fruits = ("apple","orange","mango")
print(fruits[0])

#print the last element
numbers = (1,2,3,4,5,6,7)
print(numbers[6])

#counts how many times an element appears
name = ("Anuja","Gauri","Anuja")
print(name.count("Anuja"))

#find index of an element
colors = ("Red","Green","yellow","Blue")
print(colors.index("Green"))

#checks if an element exists (using ifelse)
colors = ("Red","Pink","yellow","Blue")
if "Red" in colors:
    print("Found")
else:
    print("Not Found")

#concatenate two tuples
t1 = (1,2,3,4,5)
t2 = (9,8,7,6,5)
result = t1 + t2
print("Result =",t1 + t2)
print(result.index(7))
print(result.count(5))

#repeat a tuple
t = ("Hii",)
print(t * 3)

#find maximum and minimum
tuple = (1,2,3,4,5,6,7,8)
print(max(tuple))
print(min(tuple))
print(tuple * 6)
print(tuple.index(6))
print(tuple.count(5))
print(tuple[5])
print(tuple[0:7])

#find the sum of tuple element
tuple = (1,2,3,4,5,6,7,8)
print(sum(tuple))

#print all element
fruits = ("apple","mango","bannana")
for item in fruits :
    print(item)

#create tuple of 5 cities and print the third city
cities = ("Nagpur","Nandanvan","Itwari","Sadar")
print(cities[3])

#find the length of the tuple containing 8 numbers
numbers = (1,4,3,5,8,2,6,9)
print(len(numbers))

#count how many times 7 apperas in (7,2,7,5,7,9)
t = (7,2,7,5,7,9)
print(t.count(7))

#find the index of python in ("C","C++","python","java")
langugae = ("C","C++","python","java")
print(langugae.index("python"))

#check whether orange is presnet in ("apple","banana","mango")
fruits = ("apple","banana","mango")
if "orange" in fruits :
    print("Orange is present")
else:
    print("Not Found")

#join (1,2,3) and (4,5,6)
t1 = (1,2,3)
t2 = (4,5,6)
join = t1 + t2
print(join)

#repeat ("Hello",) four times
text = ("Hello",)
print(text * 4)

#find maximum,minimum and sum of (12,25,8,30,15)
numbers = (12,25,8,30,15)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#print each element of ("Pen","Book","Bag") one by one
elements = ("Pen","Book","Bag")
for item in elements :
    print(item)

#create a tuple of your favorite subject and print the last subject
fav_subjects = ("programming","apttitude","maths","CAD")
print(fav_subjects[3])





