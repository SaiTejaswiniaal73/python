#
# str1[14]
# Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# HELLO
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     HELLO
# NameError: name 'HELLO' is not defined
# "HELLO
# SyntaxError: unterminated string literal (detected at line 1)
# "HELO"
# 'HELO'
# HI
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     HI
# NameError: name 'HI' is not defined
# LEN(HELLO)
# Traceback (most recent call last):
#   File "<pyshell#4>", line 1, in <module>
#     LEN(HELLO)
# NameError: name 'LEN' is not defined
# LEN("hi")
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     LEN("hi")
# NameError: name 'LEN' is not defined
# len("hi")
# 2
# str1="helllo here sry"
# str1[0]
# len(str1)
# str1[14]
# SyntaxError: multiple statements found while compiling a single statement

# str1="helllo here sry"

# str1[0]
# 'h'
# len(str1)

# 15
# str1[14]

# 'y'
# str1[10]
# 'e'
# str1[11]
# ' '
# str1[-2]
# 'r'
# str1[-15]
# 'h'
# str1[1][3]
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     str1[1][3]
# IndexError: string index out of range
# str1[1],[3]
# ('e', [3])
# str[0:4]
# Traceback (most recent call last):
#   File "<pyshell#18>", line 1, in <module>
#     str[0:4]
# TypeError: type 'str' is not subscriptable
# str1[0 3
     
# SyntaxError: '[' was never closed
# str1[0 3]
     
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# str1[0:3]
     
# 'hel'
# str[-1:-5]
     
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     str[-1:-5]
# TypeError: type 'str' is not subscriptable
# ]str[-5:-1]
# SyntaxError: unmatched ']'
# str1[-5:-1]

# 'e sr'
# str1[-1:-5:-1]
# 'yrs '
# str[:]
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     str[:]
# TypeError: type 'str' is not subscriptable
# str1[:]
# 'helllo here sry'
# "1234"+2
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     "1234"+2
# TypeError: can only concatenate str (not "int") to str
# "123"+"2312"
# '1232312'
# "123"*3
# '123123123'
# "123"*-1
# ''
# 123/0
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     123/0
# ZeroDivisionError: division by zero
# 0/9
# 0.0
# str1[-13:2:-1}
# SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
# str1[-13:2:-1]
# ''
# str1[-10:2:-1]
# 'oll'




# print(5)
# print(5+2)
# print(5-2)
# print(5*3)
# print(5/2)
# print(5%3)
# print(5//2)
# print(5**2)
# a=1231
# b=1234
# x=a+b
# print(x)
# "hello"
# str1="helllo here sry"
# str1[0]
# len(str1)

# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# print("num1")
# print("num2")
# print(num1+num2)
# # teja_swini-snakecase
# #HumanBeign-
# print(type(num1))
print(int(24==44))

cj2=2+3j
cj3=3+4j
res=cj2+cj3
print(res)

# list=[1,2,3,4,"string",[1,2,3]]
# print(list[2])
# list[3]="hastring"
# print(list)

# tuple=(1,2,3,4,4,5)
# rng =range(20,0,-1)
# rng=list(rng)
# print(rng)

# for i in range(0,20):
#     print(i)

rng =range(20,0,-1)
# rng=list(rng)
print(type(rng))

rng =range(20,0,-1)
rng=list(rng)
print(type(rng))



# list1=[1,2,3,4,5,]
# print(list1(string))
# x=6
# y=6
# print(id(x))
# print(id(y))

# z=4
# z+=5
# print(x+y)
# print(z)
# str1="abc"
# str2="abc"
# # str2[1]="f"
# print(id(str1))
# print(id(str2))
# # str3=str2[1]='h'
# print(str3)

# num1=4
# num2=3
# num2+=5
# num1-=2
# num3=6
# num4=7
# num3**=2
# num4*=2
# num5=98
# num5/=3
# num6=45
# num6%+4
# print(num2)
# print(num1)
# print(num3)
# print(num4)
# print(num5)
# print(num6)

# print(2 and 3)
# print(3 and 2)
# print(3 and 0)
# print(0 and 3)
# print(1 and 3)
# print(3 and 3)
# print(False and 3)

# print(3 or 4)
# print(0 or 4)
# print(True or 0)
# print(False or 0)
# print(-2 and 3)
# print(-2 or 0)
# print(10 and -5)
# print(-2 or 3)
# print(-2 and 0)
# print(10 or -5)

# print(not 2==4)
# print(not 2!=5)
print(bin(27))
print(oct(27))
print(hex(27))

print(bin(13))

print(0x1b)
# print(5&3)#5=0101 & 3=0011
# print(5|3)#5=0101 & 3=0011
# print(5^3)#5=0101 & 3=0011
# print(~5)#5=0101 & 3=0011
# a = 5  # Binary: 0101
# result = a << 14  # Binary: 10100 -> Decimal: 20
# print(result)  # Output: 20
# print(13>>1)
# print(13<<1)
# print(13>>2)
# print(13<<2)

# x=8
# if x>=5:
#     print("great")

# y=2
# if y<=5:
#     print("less")
# else:
#     print("great 5")

# z=5
# if z<5:
#     print("less")
# elif z==5:
#     print("same")
# else:
#     print("great 5")

# name="teja"
# if name=="swini":
#     print('same or')
# else :
#     if name=="teja":
#         print("same")
#     else:
#         print("oka")

# x=34
# if x>0:
#     print("postive")
# elif x==0:
#     print("zero")
# else:
#     print("negative")

# x=-34
# if x>0:
#     print("postive")
# elif x==0:
#     print("zero")
# else:
#     print("negative")

# x=0
# if x>0:
#     print("postive")
# # elif x==0:
# #     print("zero")
# else:
#     print("negative")

# x=0
# if x>0:
#     print("postive")
# elif x==0:
#     print("zero")
# else:
#     if x<0:
#         print("negative")
#     else:
#         print("zero")

# for i in range(1,20):
#     if i%2!=0:
#         print(i,"even")
#     else:
#         print(i,"odd")
    
# list=[1,2,3,3,4,5,6]
# for i in list:
#     if list[i]==5:
#         print("5 is there")
#         break  
#     else:
#         print("5 is not found")

x=0
if x>=0:
    print("postive")
elif x==0:
    print("zero")
else:
    if x<0:
        print("negative")
    else:
        print("zero")


# list=[]
# for i in list:
    
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")
# i=0
# while i <5:
#     print(i)
#     i+=1#i=i+1
#     #but not  i++


# i=0
# while i<5:
#     if i%2==0:
#         print(i)

# i=0
# while i<5:
#     print(i)
#     i=i+2

# print("odd")
# i=1
# while i<5:
#     print(i)
#     i=i+2

# i=-10
# while i<20 :
#     # i=i+1
#     if i>0:
#      print(i,"postive")
#     elif i==0:
#         print(i,"zero")
#     else:
#         print(i,"negative")
#     i=i+1

# for i in range(0,10):
#     print("pass")
#     if i==5:
#         break
#     print(i)

# 26-1-24
# count=0
# for i in range(0,5):
#     count+=1
#     if i>=3:
#         break
#     print(i)
# print("count",count)


# for i in range(0,5):
#     count+=1
#     if i>=2:
#         continue
#     print(i)
# print("count",count)

# for i in range(0,5):
#     print(i)
#     continue    
#     print(i)

# num1=22
# if num1%2==0:
#     pass
# else:
#     print("odd")

# units=int(input("what is your unit count"))
# if units<350:
#     amount=units*20
#     print(amount)
# elif units>350 and units<=500:
#     amount=units*30
#     print(amount)
# else:
#     amount=units*50
#     print(amount)

# units=int(input("what is your unit count"))
# if units<200:
#     print(units*2,"free bill")
# elif units>=200 and units<350:
#     print("please pay the amount",units*2)
# elif units>=350 and units<450:
#      print("please pay the amount",units*3)
# else:
#     print("please pay the amont",units*4)

# units=int(input("what is your unit count"))
# if units<350:
#     if units<200:
#         if units<100:
#             print(units*-5)
#         else:
#             print("0")
#     else:
#         print(units*10)
# else:
#     print(units*240)

for i in range(1,11):
    print("class",i)
    for i in range(1,6):
        print(i)



# for i in range(1,11):
#     for j in range(1,31):
#         if i==7:
#             continue
#         print(i,j)

# for i in range(1,5):

#     for j in range(1,5):
#         if ( i==3 or i==4) and j>2 :
#             #to skip after 15
#             continue
#         print(i,j)


# for i in range(1,11):
#     for j in range(1,31):
#         if ( i==7 and j>15) or (i==8 and j>20):
#             #to skip after 15
#             continue
#         print(i,j)

# for i in range(1,11):
#     if  i>6:
#         continue
#     for j in range(1,8):
#         print(i,j)

# for i in range(1,11):
#     if  i>6:
#         break
#     for j in range(1,8):
#         print(i,j)
# count=0
# for i in range(1,11):
#     print(i)
#     for j in range(1,5):
#         count +=1
#         print(i,j)
#     break
# print(count)
# for i in range(1,11):

i=0

while i<10:
    i=i+1
    j=1
    while j<9:
        print(i,j)
        j+=1
   
   

# for i in range(1,11):#class
#     if i==7:
#         continue
#     for j in range(1,5):#roll numbers
#         print(i,j)

# for i in range(1,11):#class
   
#     for j in range(1,5):#roll numbers
#             if i==7:
#                 continue
#             print(i,j)

# for i in range(1,11):#class
#     for j in range(1,11):#roll numbers
#             if (i==7  or i==8) and j>4:
#                 continue
#             print(i,j)

count=0
i=0
while i<10:
    print(i)
    if i==7:
        i=i+1
        continue
    i=i+1
    j=1
    while j<31:
        print(i,j)
        j+=1
    print(j)
# list1=[1,2,3,4,5,23,-23,100]
# sum=0
# count=0
# for i in list1:
#     sum=sum+i
#     count+=1
# print(sum)
# if count==0:
#     print("empty list")
# else:
#     print(sum/count)

# list2=[[1,2,3,4],[5,23],[-23,100,34],[3,4,5,6]]
# sum=0
# for i in list2:
#     # print(i)
#     for j in i:
#         # print(j)
#         sum=sum+j
# print(sum)
    
# function

# print("started")
# print(4/3*3.14*10*10*10)
# print("ended")

# print("started")
# print(4/3*3.14*20*20*20)
# print("ended")

# print("started")
# print(4/3*3.14*30*30*30)
# print("ended")

#we have to write every time in change of radius

# using function

# def calc_volume(r):
#     print("started")
#     print(4/3*3.14*r*r*r)
#     print("ended")

# calc_volume(20)
# # calc_volume(30)

# def calc_volume(r,pie):
#     print("started")
#     print(4/3*3.14*r*r*r)
#     print("ended")

# calc_volume(20,23)

# def calc_volume(r,pie=3.14):
#     print(pie)
#     print(4/3*3.14*r*r*r)  
# calc_volume(20,23)
# calc_volume(10)

# defalut paramenter should be at last only any time
#funtion with return callled as normal
# giving the aruguments
# def calc_volume(r,pie=3.14):
#     print(pie)
#     return (4/3)*3.14*r*r*r
# result =calc_volume(20,23)
# print(result)

# def sum(a,b):
#     return a+b
# print(sum(3,5))

def sum(a,b,*c):
    print(type(c))
    sum=a+b
    for i in c:
        sum=sum+i
    return sum
print(sum(3,5,3,4,5,6,8,8,6,8))

# def sum(**args):
#     print(type(args))
#     print(args)
#     sum=0
#     for i,j in args.items():
#         sum=sum+j
#     return sum
# print(sum(num=3,num1=4,num2=5,num3=5))


# def sum(a,b,*c):
#     print(type(c))
#     sum=a+b
#     for i in c:
#         sum=sum+i
#     return sum
# print(sum(3,5,3,4,5,6,8,8,6,8))

#scope
#global scope
# num1=10
# print(num1)
# def trail():
#     print(num1)
# trail()
#loacl

# num1=25
# def trail():
#     num1=10
#     a=20
#     print(num1)
# trail()
# print(num1)


def sum(a,b):
    return a+b
print(sum(3,4))

#functions-void,normal,functions
#postions arugument,default arugments
#recursion function
# def fact(n):
#     print(n)
#     return n*fact(n-1)
# fact(4)-more recusrion has done

# def fact(n):
#     if n==1:
#         return 1
#     # print(n)
#     return n*fact(n-1)
# print(fact(3))

# def print_nums(n):
#     if n==0:
#         return
#     print_nums(n-1)
#     print(n)
# print_nums(10)


# decorators

def function_decorator(func):
    def wrapper():
        print("please chck a4")
        func()
        print("tq")
    return wrapper


@function_decorator
def printer():
    print("priniting-------------")

printer()

# def multiply(a,b):
#     if b==1:
#         return a
#     res=a+multiply(a,b-1)
#     print(res)
#     return res
# print(multiply(5,6))

#decorot

# def sleep(func):
#     def wrapper1():
#         print("r u sleep")
#         func()
#         print("not slpet?")
#     return wrapper1
# @sleep
# def s():
#     print("okay sleep")
# @sleep
# def w():
#     print("okay walk")
# s()
# w()

#lambda fucntion

# lambda x:x*x

# exa_lambd=lambda x:x*x
# print(exa_lambd(5))
# print(exa_lambd(2))
# print(exa_lambd(3))

#map
list1=[2,3,4,5,5,6,7,]
# def squre(x):
#     return x*x
# def multiply_5(y):
#     return y*3
# print(list(map(squre,list1)))
# print(list(map(lambda x:x*5,list1)))
 
def  check_even(x):
    if x%2==0:
        return True    
    return False

print(list(filter(check_even,list1)))
print(list(filter(lambda x:x%2==0,list1)))

# def squre(x):
#     return x*x
# lambda x:x*2
# #map,filter
# list_ex=[2,3,4,5,6,7,24,11,13]

# print(list(map(lambda x:x*x,list_ex)))

# #reduce-higherorder function
# from functools import reduce
# print(reduce(lambda x,y:x+y,list_ex))
# inbuild function-print le..
#string inbuild function
str1="collections of characterts"
str2="  collec,tion,  s of     characterts"
print(str1[2])
print(len(str1))
for i in str1:
    print(i)
print(str1[4:12])
print(str1[-11:-1])

# len().lower,upper,swapcas
print(str1.swapcase())
print(str1.upper())
print(str1.lower())
print(str2.strip())
print(str1.find("s"))
print(str1.find("z"))
print(str1.count("c"))
print(str1.startswith("coq"))
print(str1.endswith("ers"))
print(str1.replace("collection","collected"))
print(str2.split(","))
print(str1.split())
fruits = ['apple', 'banana', 'cherry']
result = ', '.join(fruits)
print(result)  # Output: "apple, banana, cherry"
digits = ['1', '2', '3', '4']
result = ''.join(digits)
print(result)  # Output: "1234"

#upto class1-15-1-01-2025

