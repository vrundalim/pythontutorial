# for i in range(0,9):
#     print(i)

#****
#****
#****
# for i in range(0,3):
#     for j in range(0,4):
#         print("*",end = " ",)
#     print()

#print a factorial number 
# factorial 
g = int(input("enter anumber :"))
og = g
a = 0
fact = g
for b in range(g):
       if fact > 0:
          c = fact % 10
      
      
          f = 1
          for i in range(1,c+1):
            f = f * i

          a += f
          fact //=10

       else:
          f   = 0 

if a == og:
    print("its a factorial number ")
else:
    print("it's not factorial number",a) 



# for e in range(0,4):
#     for h in range(0,4):
#         print("*")
#     print("_")  



    
# n = 1
# for i in range(1, 5):          # rows
#     for j in range(i):         # numbers per row
#         print(n, end=" ")
#         n+=1
#     print()

# # to print hollow square
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # to print addtion sign
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 3  or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



               
# for i in range(1,6):
#     for  j in range(4,i-1,-1):
    
#         print("*",end = " ")
#     for k in range(1,i+1,+1):
#         print("*",end = " ")
#     print()
    

# # while loop 
# # palidrome
# # fibonaci
# # armstrong
# # spy
# # neon
# # factorial

# # conditional 
# # comapre
# # for loop
# # pattern

