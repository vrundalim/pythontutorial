# a = int(input("enter a number :"))
# b = 0
# while a > 0 :
#  c =   a % 10 
#  b +=c
#  a //= 10
# print("total of a is :",b)


# a = int(input("enter a number :"))
# b = 0 
# while a > 0 :
#   c = a % 10 
#   b = b * 10 + c
#   a  = a // 10

# print("reverse number is :",b)

# c = int(input("enter a number :"))
# a = 0
# while c > 0 :
#     d =  c % 10 
#     a = a * 10  + d
#     c //= 10
#     if a == c:
#      print("reverse number :",a)
        


#check if number is neon or not means if numbers 
# digits 9*9 = 81 then 8+1 = 9 then 9 is neon numbers
# a = int(input("enter a number:"))
# b =  a * a
# og = b
# f = 0
# while og > 0 :
#       c = og % 10
#       f += c
#       og //=10

# if  a == f:
#    print("it's neon number")
# else:
#    print("it's not a neon number")



#check number is spy or not means
#if number  digits multiply and sum are same then spy otherwise not
# a = int(input("enter a number:"))
# og = a
# b = 1
# while og > 0 : 
#    c = og % 10
#    b =  b  * c
#    og //= 10
#    v = b
#    f = 0
#    while og > 0 :
#       c = og % 10
#       f += c
#       og //=10
      
# if  v == f:
#    print("it's spy number")
# else:
#    print("it's not a spy number",v)

# n=  34
# for  i in range (1,11):
#    for  j in range(i,n+1,10):
#       print(j,end = " ")
      
#    print()


# for  j in range(1,5):
#    for  k in range(1,j*2,2):
#       print(k,end = " ")
#    print()

   
n = 1
for k in range(1,4):
   for  l in range(1,n+1,5):
      print(l,end = " ")
   print()
