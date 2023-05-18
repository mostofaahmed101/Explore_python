# #  n একটি সংখ্যা , এটি জোড় নাকি বিজোড়
# 
# n = int(input("Enter your number "))
# 
# if n%2 == 0:
#     print(n, "is an Even Number")
# else:
#     print(n, "is an odd Number")
# #     
#     
# 
# 
# 
# # দুটি সংখ্যার মধ্যে বড় এবং ছোট সংখ্যাটি বের করো ।
# 
# num1 = int(input("Enter your first Number "))
# num2 = int(input("Enter your 2nd Number "))
# 
# if num1>num2:
#     print(num1, "is the highest Number And",num2, "is the Lowest Number")
# else:
#     print(num2, "is the highest Number And", num1,"is the Lowest Number")
# 
# 
# 
# 
# #  n একটি সংখ্যা এটি positive Number নাকি Negative Number, output এ দেখাও ।
# 
# N = int(input("Enter Your Value for N : "))
# 
# if N>0:
#     print(N,"is an Positive Number")
# elif N==0:
#     print("Your value is Equal to Zero(0)")
# else:
#     print(N,"is an Negative Number")
# 
# 
# 
# 
# # দুইটি সংখ্যার যোগফল বের করার প্রোগ্রাম।
# 
# Number1, Number2 = int(input("Enter your 1st Number : ")),int(input("Enter your 2nd Number : "))
# print("The Total Number of your Value is", Number1 + Number2)
# 
# 
# 
# 
# # দুইটি সংখ্যার বিয়োগফল বের করার প্রোগ্রাম।
# 
# Number1, Number2 = int(input("Enter your 1st Number : ")),int(input("Enter your 2nd Number : "))
# print("The Total Number of your Value is", Number1 - Number2)
# 
# 
# 
# 
# # সমকোণী ত্রিভুজের ক্ষেত্রফল নির্নয়ের প্রোগ্রাম।
# 
# base = float(input("Enter the value of base : "))
# height = float(input("Enter the value of Height : "))
# Area = 1/2 * base * height
# print("The Area of the triangle is",Area)
# 
# 
# 
# 
# # ত্রিভুজের ক্ষেত্রফল নির্নয়ের প্রোগ্রাম।
# 
# a=float(input("Enter value for A : "))
# b=float(input("Enter value for B : "))
# c=float(input("Enter value for C : "))
# if a+b>c and b+c>a and a+c>b:
#     s = (a+b+c)/2
#     Area=(s*(s-a)*(s-b)*(s-c))**.5
#     print("Area of the Triangle is", Area)
# else:
#     print("Error!! Wrong value")
# 
# 
# 
# # ৩ টি সংখ্যার মধ্যে বড় সংখ্যা বের করার প্রোগ্রাম।
# 
# A=float(input("Enter value for A : "))
# B=float(input("Enter value for B : "))
# C=float(input("Enter value for C : "))
# if A>B and A>C:
#     print(A,"is the larger Number")
# elif B>A and B>C:
#     print(B,"is the larger Number")
# else:
#     print(C,"is the larger Number")
# 
# 
# 
# 
# # আয়তক্ষেত্রের ক্ষেত্রফল নির্নয়ের প্রোগ্রাম
# 
# length=float(input("Enter the value for Length : "))
# width=float(input("Enter the value for Width : "))
# Area= length*width
# print("Area of Rectangle is",Area)
# 
# 
# 
# 
# # ১ - ১০০ এর মধ্যে জোড় সংখ্যাগুলো Print করার programme লেখ ।
# 
# for i in range(2,101,2):
#     print(i)
#         # অথবা
# for i in range(1,101):
#     if (i%2)==0:
#         print(i)
#         
# 
# 
# 
# 
# 
# # ১ - ১০০ এর মধ্যে বিজোড় সংখ্যাগুলো Print করার programme লেখ ।
# 
# for i in range(1,100,2):
#     print(i)
# 
# 
# 
# # বৃত্তের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম
# 
# r = float(input('Enter value for Radius : '))
# pi = 3.1416
# print('Area of Circle =', pi*r*r)
# 
# 
# 
# # ধনাত্বক পূর্ণ সংখ্যার ফ্যাক্টোরিয়াল এর মান

# n=int(input('enter the value '))
# x=1
# if n>1:
#     for i in range(n,1,-1):
#         x*=i
#     print('the value of factorial is',x)
# elif n==0 or n==1:
#     print('the value of factorial is 1')
# else:
#     print('Negative factorial is not possible')


# 
# # Grade নির্নয়ের প্রোগ্রাম
# 
# n=int(input('Enter your average Number : '))
# if n>=80:
#     print('GPA 5.00 (A+)')
# elif n>=70:
#     print('GPA 4.00 (A)')
# elif n>=60:
#     print('GPA 3.50 (A-)')
# elif n>=50:
#     print('GPA 3.00 (B)')
# elif n>=40:
#     print('GPA 2.00 (c)')
# elif n>=33:
#     print('GPA 1.00 (D)')
# else:
#     print('Fail (F)')


# 
# 
# # fahrenheit to Celsius
# 
# F = float(input('fahrenheit : '))
# C = ((F-32)*5)/9
# print('Celsius',C)
# 
# 
# # Celsius to fahrenheit
# 
# C = float(input('Celsius : '))
# F = ((C*9)/5)+32
# print('fahrenheit',F)
# 
# 
# # দ্বীঘাত সমীকরণ
# 
# a=int(input('a : '))
# b=int(input('b : '))
# c=int(input('c : '))
# d = (b*b)-(4*a*c)
# if d>0:
#     x1 = ((-b)+(d*d))/(2*a)
#     x2 = ((-b)-(d*d))/(2*a)
#     print('x1 =',x1,'\nx2 =',x2)
# elif d==0:
#     x = (-b)/(2*a)
#     print('x1 =',x,'\nx2 =',x)
# else:
#     print('Negative Square-Root is not possible')
# 
#     
# 
# # 1^2 + 2^2 + 3^2 +.....+n^2 এর যোগফল
# 
# n=int(input('n : '))
# y=0
# x=0
# for i in range(1,(n+1)):
#     x+=i
#     y+=(i*i)
# print('sum =',x)
# print('sum of square =',x**2)
# print(y)
# 
# 
# 
# # মৌলিক সংখ্যা বের করার প্রোগ্রাম
# 
# Serial = int(input('value for N : ')) + 1
# 
# n = 1
# while (n<=Serial):
#     x =0
#     i=2
#     while (i<= n//2):
#         if (n%i == 0):
#             x +=1
#             break
#         i+=1
#     if (x==0 and n !=1):
#         print(n, end = '  ')
#     n+=1









































# x,y = 5,10
# x,y = y,x
# print(x)
# print(y)
# 
# print((0)**0.5)
# 
# x,y=23,5
# print(x%y)
# 
# 
# 
# 
# # Leap Year বের করার প্রোগ্রাম
# 
# year = int(input('Enter year : '))
# if (year%4)==0:
#     if (year%100)==0:
#         if (year%400)==0:
#             print(year,'is a Leap Year')
#         else:
#             print(year,'is not a Leap Year')
#     else:
#         print(year,'is a Leap Year')
# else:
#     print(year,'is not a Leap Year')
#     
# #                 অথবা
# y = int(input('which year : '))
# if (y%4)==0:
#     print(y,'is a leap year')
# else:
#     print(y,'is not a leap year')
#     
#     
# 
# 
# 
# 
# 
# 
# 
# # ফাংশন ব্যাবহার করে
# 
# def func():
#     x=0
#     for i in range(5,151,5):
#         x+=i
#     return x
# print(func())
# 
# 
# 
# a=10
# b=2.7
# print(a/b)
# print(a//b)
# 
# 
# 
# l = ['kalu','aalu','balu',26,'kalu']
# l2 = ['suuu','siu']
# l.append('talu')
# l.insert(1,'salu')
# l.pop(4)
# l.remove('balu')
# l.sort()
# l[-1]= "malu"
# # print(l)
# 
# 
# di ={'aa':16,'ba':23, 'sa':99, 55:'laa'}
# # print(di)
# 
# s = {20,10,'lala',"dala"}
# s2 = {'sala','lala','gala'}
# s.add('jala')
# s.remove(20)
# print(s)


































                                             # 3rd Semester
                            # Basic Application Development Using Python









# Date and time syntex
import datetime
dt = datetime.datetime.now()


# date or today syntex
from datetime import date
d = date.today()
# print(d)


# time syntex
from datetime import time

import time
t = time.localtime()
# print(t)


# print(t0)



# file
file = open("for py file test.txt", "w+")
# file.write("mor\nar\nbala\nlage\nna")
file.close



