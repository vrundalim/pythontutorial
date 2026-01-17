# print the max number based on the 3 number 
#  a = int(input("enter a first num :"))
# b = int(input("enter a second num :"))
# c = int(input("enter a third num :"))
# if a > b :
#     if a > c :
#         print("a is max",a)
#     else :
#         print("c is max",c)
# else :
#     if b >c :
#         print("b is max",b)
#     else :
#         print("c is max",c)


# smallest of 2 number
# a = 38
# b = 36
# print("a is smallest ",a) if a < b else print("b is smallest",b)


# check voting eligibility
# age   = int(input("enter a age :"))
# if age <= 18 :
#     print("you are eligible to vote")
# else :
#     print("you are eligible to vote")


#check the even and odd number
# a = int(input("enter a number :"))
# if a % 2 == 0:
#     print("a is even num ",a)
# else:
#     print("a is odd num ",a)


#check the positive ,negative and zero number
# a = int(input("enter a number :"))
# if a > 0:
#     print("a is positive ",a)
# elif  a < 0:
#     print("a is negative",a)
# else:
#     print("a is zero value")


#student result
# print("*****Student's Result*****")
# marks = int(input("enter a marks :"))
# if marks >= 90 and marks <=100:
#     print("Grage is A")
# elif marks >= 75 and marks <=89:
#     print("Grage is B")
# elif marks >= 50 and marks <=74:
#     print("Grage is C")
# else:
#     print("Failed")


#calculator 
# print("*****Calculator*****")
# print("Press 1 for Addition ")
# print("Press 2 for Substraction ")
# print("Press 3 for Division ")
# print("Press 4 for Multiplication ")
# a = int(input("enter a  number for the opration :"))
# if  a == 1:
#  b =  int(input("enter a  1st number :"))
#  c =  int(input("enter a  2nd number :"))
#  d = b+c
#  print("The Addition of two numbers is :",d)
# elif  a == 2:
#  b =  int(input("enter a  1st number :"))
#  c =  int(input("enter a  2nd number :"))
#  d = b-c
#  print("The Substraction of two numbers is :",d)
# elif  a == 3:
#  b =  int(input("enter a  1st number :"))
#  c =  int(input("enter a  2nd number :"))
#  d = b%c
#  print("The division  of two numbers is :",d)
# elif  a == 4:
#  b =  int(input("enter a  1st number :"))
#  c =  int(input
# ("enter a  2nd number :"))
#  d = b*c
#  print("The Multiplication of two numbers is :",d)
# else :
#  print("please enter the number  1 to 4")


#check number is divied by 3 and 7 or not
# a = int(input("enter a number :"))
# if a % 3 == 0 and a % 7 ==0 :
#     print("a is divied by 3 and 7")
# elif a % 3 != 0 or  a % 7 == 0:
#     print("a is only divied by 7")
# elif a % 3 == 0 or  a % 7 != 0:
#     print("a is only divied by 3")
# else:
#     print("a isn't divisible")


#while loop print reverse number 
# a = int(input("enter a number :"))
# while a >= 1:
#     print("reverse number :",a) 
#     a -= 1
 
# using while sum all the printed numbers
c = 0
a = int(input("enter a number :"))
while a > 0:
    b = a % 10
    c += b
    a //= 10
print("total number is :",c)

#counting the numbers based on the input numbers
# b = 0
# a = int(input("enter a number:"))
# while a > 1 :
#    c = a % 10 
#    b = b + 1
#    a //= 10
# print("total digit of number is",b)


#addtion  the even  numbers based on the input numbers
# b = 0
# d = 0
# a = int(input("enter a number:"))
# while a > 0 :
#    c = a % 10
#    b =  c
#    a //= 10 
#    if b % 2 == 0:
#      d += b
# print("total addtion of even num is",d)

#addition  the numbers based on the input numbers
# b = 0
# a = int(input("enter a number:"))
# while a > 1 :
#    c = a % 10 
#    b = b + c
#    a //= 10
# print("total digit of number is",b)


#palidrome num
# b = 0
# a = int(input("enter a number:"))
# d = a
# while a > 0:
#    c = a % 10 
#    b = b * 10 + c 
#    a //= 10
#    if d == b :
#     print("its palidrome number :")
# else:
#    print("it is not palidrome num")

   
#print the palidrome number of 1000 to 1
# a = 1000
# while  a >= 1 :
#     e = a
#     b = 0
#     while e > 0 :
#        c = e % 10  
#        b = b * 10 + c
#        e //= 10   
#     if a == b:
#       print(b)

#     a -=1



# a = 1
# b = int(input("enter a number "))
# while a <= 10:
#    print(f"{b} * {a} = {b*a}")
#    a +=1

#check the after factorial number will same as original
a = 145
e = 0
g = a
while a > 0 :
      c = a % 10

      f = 1
      while c > 0:
         f = f*c
         c -=1

      e += f
      a //=10

if e == g:          
 print(e)
else:
 print("") 

# print 1 to 1000 palidrome number
# a = 1
# while  a <=1000 :
#     e = a
#     b = 0
#     while e > 0 :
#        c = e % 10  
#        b = b * 10 + c
#        e //= 10
#     if a == b:
#       print(a)
     
#     a  +=1


 # print a number where 0 should be == 9 
# a = int(input("enter a number: "))
# rev = 0
# b = a
# while b > 0:
#     c = b % 10
#     if c == 0:
#         c = 9
#     rev = rev * 10 + c
#     b //= 10
# result = 0
# while rev > 0:
#     result = result * 10 + (rev % 10)
#     rev //= 10

# print(result)

#armstrong numbers  like suppose there is number 9 it has 1 digit 
# then it multiple 981 and 98 number has 2 digit then each has to
#  multiply by 2 then if it same  as original number then its armstrong otherwsie not
# a = 9
# og = a
# h = 0
# f = a
# while f> 0 :
#      h +=1
#      f //= 10  
# sum = 0
# while a >0:
#       c = a % 10
#       g = 1
#       i = h
#       e = 0
#       while i > 0:
#             g = g *c
#             i-=1
#       sum = sum + g
#       a//=10
# if sum == og:
#     print("its a armstrong",sum)
# else:
#     print("no")


