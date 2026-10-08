#create a list of 5 fruits and print it
fruits = ["apple","mango","banana","orange","graphes"]
print(fruits)

#print the first element 
fruits = ["apple","mango","banana","orange","graphes"]
print(fruits[0])

#print the last element
fruits = ["apple","mango","banana","orange","graphes"]
print(fruits[4])

#print the third element
list = [1,2,3,4,5,6]
print(list[2])

#find the length
list = [1,2,3,4,5,6]
print(len(list))

#check whether apple is present
fruits = ["apple","mango","banana","orange","graphes"]
if "apple" in fruits :
    print("apple is present")
else :
    print("apple is not present")

#check whether 25 is present
l1 = [2,3,54,65,8,7,25]
if 25 in l1 :
    print("25 is present")
else :
    print("25 is not present")

# print all element using loop
name = ["Anuja","Komal","Janvahi"]
for name in name :
    print(name)

#add an element using append
list = [1,23,4,5,6,7,8]
list.append(45)
print(list)

#insert an element at index 2
fruits = ["mango","banana","apple"]
fruits.insert(2,"orange")
print(fruits)

# remove an element using remove()
numbers = ["mango","banana","apple"]
numbers.remove("mango")
print(numbers)

# clear all element using clear()
list = ["mango","banana","apple"]
list.clear()
print(list)

# find the index of an element
list = ["mango","banana","apple"]
print(numbers.index("banana"))

# count how many times an element appear
list = [1,2,3,4,5,61,23,4,5,6,7,8]
print(list.count(5))

# change the second element
fruits = ["banana","apple","mango"]
fruits[1] = "orange"
print(fruits)


marks = [12.2,34.3,56.4,78.6,98.76,98.09,76.98,95.03]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[5])
print(len(marks))

#list slicing
marks = [ 98,87,67,45,96,83,78]
print(marks[1:5])
print(marks[1:3])
print(marks[:3])
print(marks[2:])
print(marks[-1::-3])

# 1.WAP to ask the user to Enter names of their 3 favorite movies & store them in a lis/
movies =[]
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# OR

movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)


# 2.WAP to check if a list contains a Palindrome of elements.(Hint:use copy() method)

list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
print(list1)
copy_list2 = list2.copy()
copy_list2.reverse()
print(list2)

#Check the list is palindrome or not
if(copy_list1 == list1):
    print("list 1 is Palindrome")
    if(copy_list2 == list2):
        print("List2 is palindromic ")
    else:
        print("list2 is not palindromic")    
else:
    print("list 1 is NOT Palindrome")
list3 = ["m","a","a","m"]
copy_list3 = list3.copy()
copy_list3.reverse()
print(list3)
if(copy_list3 == list3):
    print("list 3 is Palindrome")
else:
    print("list 3 is NOT Palindrome")





