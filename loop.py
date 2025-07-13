"""# For Loop Questions
#Print numbers from 1 to 10 using a for loop.
num=10
print("counting till 1 to 10 =\n")
for i in range (1,num+1):
    print(i)


#Print all even numbers between 1 and 50.
num =int (input("enter the no till you want even no"))
print("even nos are=\n")
for i in range (1,num+1):
    if(i%2==0):
        print(i)

#Calculate the sum of all numbers from 1 to 100.
num=int(input("enter the no "))
print(num)
sum=0
for i in range (1,num+1):
    sum=sum+i
print("total sum=",sum)
    

#Print the multiplication table of a given number (e.g., 5).
a=10
num=int(input("enter the no whose table you wanna print"))
print("table of",num)
for i in range (1,a+1):
    print(i*num)


#Print each character of a given string using a for loop.
a="AMANKUMAR"
for i in range(0,len(a)):
    print(a[i])


#Print all elements in a list using a for loop.
a=[1,'d',"aman",12.4,4+5j]
print("element in list are")
for i in range(0,len(a)):
    print(a[i])

#Print the squares of numbers from 1 to 10.
num=int(input("enter the no"))
sq=0
for i in range (1,num+1):
    sq=i**2
    print("sqare of no btw 1-10 are=",sq)
    

#Use a for loop with range() to print numbers in reverse (from 10 to 1).
num=int(input("enter the no "))
print("counting till 1 to 10 =\n")
for i in range (num,0,-1):
    print(i)
    
"""
"""#Print only vowels from a given string.
a="HIRAL SHARMA"
for i in range(1,len(a)):
    if(('a','e','i','u')in a):
        print(a[i])"""
#Print the factorial of a number using a for loop.
num=int (input("enter the no "))

for i in range (1,num+1):
    if(num%i==0):
        print(i)
        

