"""#While Loop Questions
#Print numbers from 1 to 10 using a while loop.
a=1
print("NUMBER FROM 1-10 ARE=")
while (a<=10):
    print(a)
    a=a+1
    

#Keep taking input from the user until they type "exit".
choice="Y"
while choice in "Y":
    name=input("enter the name")
    choice=input("enter you wanna continue or not (Y/N)")
    

#Print the sum of digits of a given number using a while loop.
a=1
sum=0
num=int(input("enter the no till you want sum"))
while (a<=num):
    sum=sum+a
    a=a+1
print(sum)
"""
#Count the number of digits in a given number.
i=10
num=int(input("enter the no"))
count=0
rem =0
while(i>0):
    rem=num%10
    count=count+1
    print(count)
    num=rem
        
        

"""5. Reverse a given number using a while loop.
6. Print a countdown from 10 to 1 using a while loop.
7. Print all even numbers between 1 and 50 using a while loop.
8. Keep asking the user to guess a number until they get it right.
9. Check if a number is a palindrome using a while loop.
10. Print Fibonacci sequence up to n terms using a while loop.
"""
