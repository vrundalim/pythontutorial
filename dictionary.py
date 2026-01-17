student_name = ["Asha","Mina","Sikha"]
marks = {"asha" : {"eng": 78,"maths": 45, "guj" : 67},
         "mina":{"eng": 33,"maths": 99, "guj" : 78} ,
         "sikha":{"eng": 67,"maths": 88, "guj" : 75} }
total  = 0
c = 0
print(f"{student_name[1]} your result is")
for  l in marks['mina']:
    print(f"{l} : {marks['mina'][l]}")
    c = marks['mina'][l]
    total = total +  c
print("total marks : ",total)
per = total/3
print("your percantage is :",per)
if per <= 100 and per >= 91 :
    print("your overall grade is : A1")
elif per <= 90 and per >= 81:
    print("your overall grade is : A2")
elif per <= 80 and per >= 71:
    print("your overall grade is : B1")
elif per <= 70 and per >= 61:
    print("your overall grade is : B2")
elif per <= 60 and per >= 51:
    print("your overall grade is : C1")
elif per <= 50 and per >= 41:
    print("your overall grade is : C2")
elif per <= 40 and per >= 33:
    print("your overall grade is : D1")
else:
    print("your overall grade is : Fail")
# studentt_name = asha
# eng = 45
# mina = 45
# guj  = 67
# total = e+m+g
# per = total/3