a =  int(input("enter a number:"))

# #palidrome number
b = 0
palidrome = a
pe = a
while pe > 0 :
    c = pe % 10
    b = b * 10+ c
    pe //= 10 
if b == palidrome:
    print("it's palidrome number",b)
else:
    exit

# #armstrong number
ams = a
armstrong = a
ag = a 
h = 0
while armstrong> 0:
    h +=1
    armstrong //= 10  
sum = 0
while ag >0:
    c = ag % 10
    i = h
    w = 1
    while i > 0:
        w = w *c
        i-=1
    sum = sum + w
    ag//=10 
if sum == ams:
    print("its a armstrong number",sum)
else:
    exit

# #neon number
neon = a
no = a * a
eo = 0
while  no > 0 :
    c = no % 10
    eo = eo + c
    no //= 10
if eo  == neon:
    print("its a neon number",eo)
else:
    exit

# #spy number 
spy  = a
sp = a
py = 1
bb = 0
while sp > 0:
    c = sp % 10
    py = py * c
    sp //= 10
    vi = py
    spi = 0
    while spy > 0 :
       c  = spy % 10
       spi += c
       spy //= 10
       bb  = spi
if bb == vi:
    print("its spy number")
else:
     exit

#factorial 
factorial = a
fact = a
sum = 0
while factorial > 0 :
    c = factorial % 10
    ff = 1
    while c > 0 :
        ff = ff * c
        c-=1
    sum+= ff
    factorial //= 10
if sum == fact:
    print("its factorial num",sum)
else:
    exit
    
even = a

# # odd and even number
if even % 2 == 0:
    print(f"{even} is even number")
else:
   print(f"{even} is odd number")

# #divided by 3 and 5
divided = a
if divided % 5 == 0 and divided % 3 == 0:
    print(f"{divided} is divided by 3 and 5")
else:
    print(f"{divided} can't divided by 3 and 5")

#prime number
prime = a
if a % 1 == 0 and a > 1:
    print("it's a prime number",a)
else:
    print("it's not  a prime number",a)
