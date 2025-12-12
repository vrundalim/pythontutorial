"""elif statement"""
print(not(5<6))
a = int(input("enter  number a :"))
b = int(input("enter  number b :"))
c = int(input("enter  number c :"))
d = int(input("enter  number d :"))
if a>b  and a>c and a>d:
    print("Hello",a)
elif b>c and b>d:
    print("b si Max",b)
elif c>d:
    print ("C is max")
else :
    print("d is max",c)    

# ==  True false 
#   True false    -- True and  True ==  True
#   Or     False or false == False  
#    not  -- True   -- False   ... False - true

# print(not(5<6))
# a = int(input("enter  number a :"))
# b = int(input("enter  number b :"))
# c = int(input("enter  number c :"))
# d = int(input("enter  number d :"))
# if a>b  and a>c and a>d:
#     print("Hello",a)
# elif b>c and b>d:
#     print("b si Max",b)
# elif c>d:
#     print ("C is max")
# else :
#     print("d is max",c)     

"""logical opercator"""
math = int(input("enter math marks :"))
eng = int(input("enter  eng marks :"))
hindi = int(input("enter  hindi marks :"))
guj = int(input("enter  guj marks :"))
science = int(input("enter  science marks :"))
total = math + eng + hindi + guj + science
per = total/5
print("percantage is",per)
if per <= 91 and per <= 100 :
     print("grade is A1",per)
elif per <= 81 and per <= 90 :
    print("grade is A2",per)
elif per <= 71 and per <= 80:
    print("grade is B1",per)
else:
    print("grade is poor",per)


# print("enter your choice")
# print("1st is calcius to fahrenhit")
# print("2nd is fahrenhit to calcius")
# value = int(input("enter any one:"))
# if value == 1:
#     c = int(input("enter a calcius value :"))
#     f = c * 9/5+32
#     print("fahrenhit is :",f)
# elif value == 2:
#     f = int(input("enter a fahrenhit value :"))
#     c = (f - 32)/(5/9)
#     print("calcius is :",c)
# else:
#     print("enter number 1 or 2")
    
    
    # nested 
    #  ladder 
    #  logical Operator
    
    
    
# ShortHand If 
# a = 7 
# b = 4
# c = 2
# d = 14
# e = 3
# max =  print("A is max",a) if a>b and a>c and a > d and a >e else  print("B is max",b) if b>c  and b >d and b > e else print("C is max",c) if c >d and c > e else print("d is maximum",d) if d > e else print("e is maximum",e)

# a = 7 
# b = 4
# c = 2
# d = 14
# max =  print("A is max",a) if a>b and a>c and a > d  else  print("B is max",b) if b>c  and b >d else print("C is max",c) if c >d else print("d is maximum",d)
  
# // 
#  569   == 9   789  2424  365  

a = int(input("enter a number :"))
# b =  a % 10 
# print("last number of a :",b)

# if a % 2 == 0  :
#     print("a is even number",a)
# else :
#     print("a is odd number",a)

# if  a > 0 :  
#    print("b is positive")
# elif a < 0 :
#    print("b is negitive")
# else :
#     print("b is zero")
    
 
if a % 5 == 0  and a % 3 == 0:
    print("a is divided by 5 and 3 ")
else :
     print("reenter the number")   




   
                
                     
                
       
        
                     
                
        
                
                
        

                        







