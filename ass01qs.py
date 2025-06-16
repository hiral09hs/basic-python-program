"""
ARITH OPERATION :-
01 Write a Python program to input two numbers and print their sum, difference, product, and quotient.

a=int(input("enter the first no"))
b=int(input("enter the second no"))
sum=a+b
sub=a-b
product=a*b
div=a/b
print("addition=",sum)
print("subtraction=",sub)
print("multiplication=",product)
print("division=",div)

 02 #Write a program to calculate the area and circumference of a circle given the radius.
PI=3.14
rad=float(input("enter the radius"))
area=PI*rad**2
cir=2*PI*rad
print("AREA=",area)
print("circumference=",cir)

03#Write a program to calculate the average of three numbers

a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
avg=(a+b+c)/3
print("average of three numbers=",avg)

04#Write a program to swap two numbers without using a third variable.
a=int(input("enter the first no"))
b=int(input("enter the second no"))
print("a=",a)
print("b=",b)
a=a*b
b=a/b
a=a/b
print("value of A AFTER SWAP",a)
print("value of B AFTER SWAP",b)


05#Write a program that computes the power of a number using the ** operator.

a=int(input("enter the base value"))
b=int(input("enter the power value"))
pval=a**b
print("power value =",pval)
"""



"""
#LOGICAL OPERATOR:-
01#Write a Python program to check if a number is positive and even.

a=int(input("enter the number"))
print("number you entered is=",a)
print("ANSWER IS= ",a>=0 and a%2==0)

02#Write a program to check if a given number is divisible by 3 or 5.
no=int(input("enter the no to check the divisibility "))
print("number you entered is=",no)
print("ANSWER IS=",no%3==0 or no%5==0)

03#Write a program to check whether a year is not a leap year using logical not.
year=int(input("enter the no of days in the year either 365 or 366"))
print("days you have entered is=",year)
print("is year a leap year??",not year!=366)

04#Given two Boolean variables a and b, write a program to evaluate and print the result of a and b, a or b, and not a.
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
print("value of a=",a)
print("value of b=",b)
print("ANSWER IS=",a and b)
print("ANSWER IS=",a or b)
print("ANSWER IS=",not a)
"""


"""
#IDENTITY OPERATOR:-

01#Write a program to demonstrate the use of is and is not with integers.

#Example: a = 5; b = 5; print(a is b)
A=int(input("enter the value of A"))
B=int(input("enter the value of B"))
print("value of A= ",A)
print("value of B= ",B)
print("ANSWER IS=",A is B)
print("ANSWER IS=",A is not B)

02#Write a program to check whether two variables point to the same object in memory
a="Hiral"
b="Hiral Sharma"
c="Sharma"
d="Hiral"
print("1st object=",a)
print("2nd object=",b)
print("3rd object=",c)
print("4th object=",d)
print("match is exact ??",a is b)
print("match is exact ??",b is c)
print("match is exact ??",a is d)
print("match is exact ??",b is d)

03#Write a program to demonstrate is and is not with None.
#Example: x = None; print(x is None)
x=None
print("value of x=",x)
print("value of x is=",x is None)
"""



"""
#MEMBERSHIP OPERATOR:-

 01#Write a Python program to check if a character is present in a string.
str=input("enter the string")
char=input("enter the char to check present or not")
print(char in str)


02#Write a program to check if a number exists in a given list.
a=[1,2,3,4]
check=int(input("enter the number which is present in a"))
print(check in a)

03#Write a program that checks if a keyword like "data" is in a list of strings.
a=['H',"data",'J',"hiral","hs"]
check=input("enter the number to check if it is present in a")
print(check in a)

#Write a program to search for a user input in a list and return if it's "Found" or "Not Found".
a=input("enter the list")
b=input("enter to check present in a or not")
print(b in a)
"""



"""
MCQS-:
Q1. What will be the result of the following expression: 5 + 3 * 2?
(b)11

Q2. What is the output of: 10 // 3 in Python?
(c)3

Q3. Which of the following is used for exponentiation in Python?
(b)**

Q4. What will the expression 7 >= 7 return?
(a)True

Q5. Which of the following expressions is equivalent to "not equal to" in Python?
(b)!=

Q6. What is the result of 4 < 2?
(b)False

Q7. Which logical operator is used to combine two conditions where both must be true?
(c)AND

Q8. What does the expression not (True or False) evaluate to?
(b)False

Q9. What will be the result of True and False or True?
(a)True

Q10. What does the expression a is b check in Python?
(c) If a and b refer to the same object in memory

Q11. What will be the output of the following code?
python
CopyEdit
a = [1, 2, 3]
b = a
print(a is b)
(a) True

Q12. What will 3 in [1, 2, 3, 4] return?
(b) False

Q13. Which operator checks if a value is not present in a sequence?
(b) not in

Q14. Which of the following statements correctly uses a membership operator?
(c) if 5 in [1,2,3]:

"""
















