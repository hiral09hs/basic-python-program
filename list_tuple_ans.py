"""
#Create a list and tuple with the same elements. Print both.
lists=[23,2+5j,'l',"hs",23.5]
print(type(lists))
print("list is=",lists)
tuples=(23,2+5j,'l',"hs",23.5)
print(type(tuples))
print("tuple is=",tuples)


#Convert a list to a tuple and vice versa.
a=[(23,49,50,3,5)]
print(type(a))
"""




"""
#Check if a specific element exists in a list and in a tuple.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
check=int(input("enter the no present or not to check"))
if(check in (a and b)):
    print("element present in \n",a,b)
else:
    print("not present")



#Find the length of a given list and tuple.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
print(len(a))
print(len(b))



#Find the maximum and minimum values in a list and in a tuple.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
print("maximum element of list=",max(a))
print("minimum element of list=",min(a))
print("maximum element of tuple=",max(b))
print("minimum element of tuple=",min(b))


#Iterate through a list and a tuple using a for loop.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
for i in range(0,len(a)):
    print(" list =",a[i])
for i in range(0,len(b)):
    print("tuple =",b[i])


# Access and print the last element of a list and a tuple using negative indexing.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
print("last element of list is=",a[-1])
print("last element of tuple is=",b[-1])


#Add an item to a list and show that the same cannot be done to a tuple.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
print(a)
print(b)
a.append(99)
print(a)
b.append(99)
"""
    
"""
#Remove all duplicates from a list using a loop and store the result as a tuple.
a=(23,24,23,4,6,5,4,23,6,9)
for x in range(0,len(a)):
    print(a[x])
   

#Slice a list and a tuple to get every second element.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
"""
"""
# Reverse a list and a tuple.
a=[23,49,50,3,5]
b=(46,49,7,9,12,30)
print(a)
a.reverse()
print("reverse of list=\n",a)
print("reverse of tuple=\n",b[6:0:-1])

#Count how many times a given value appears in a list and in a tuple.
a=[23,49,23,50,23,5]
b=(46,49,7,49,12,30)
print(a.count(23))
print(b.count(49))
"""

#Merge two lists and two tuples respectively.
a=[23,49,23,50,23,5]
b=[46,49,7,49,12,30]
print(a)
print(b)
a.extend(b)
print(a)
c=(23,49,23,50,23,5)
d=(46,49,7,49,12,30)
print(c)
print(d)
c.extend(d)
print(c)
"""
#Find the index of a particular element in a list and tuple.
a=[23,49,23,50,23,5]
b=(46,49,7,49,12,30)
print(a.index(23,1,4))
print(b.index(49,2,5))
"""
#Write a function that takes a list of numbers and returns a tuple of (min, max, average).

"""
Given a list of tuples, sort it based on the second element in each tuple.
17. Flatten a list of tuples into a single list. Example: [(1,2), (3,4)] → [1,2,3,4]
18. Create a list of tuples representing (element, index) pairs from a given list.
19. Unpack a tuple of values into individual variables.
20. Write a program that takes a tuple with a nested list and modifies the list inside the
    tuple.
"""
