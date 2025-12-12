a = int(input("enter  number a : "))
b = int(input("enter  number b : "))
c = int(input("enter  number c : "))
d = int(input("enter  number d : "))
e = int(input("enter  number e : "))
if a > b:
    if a > c:
        if a > d:
            if a > e:
                print("a is maximum",a)
            else :
                print("e is maximum",e)
        else:
            if d >e :
                print("d is maximum",d)
            else :
                print("e is maximum",e)
    else :
        if c > d :
                if c > e:
                    print("c is maximum",c)
                else :
                    print("e is maximum",e)

        else :
            if d > e :
                print("d is maximum ",d)
            else :
                print("e is maximum",e)
else:
    if b > c:
        if b > d :
            if b > e:
                print("b is maximum",b)
            else :
               print("e is maximum",e)
        else:
         if d >e :
             print("d is maximum",d)
         else :
             print("e is maximum",e)
    else : 
        if c > d :
            if c > e : 
                print("c is maximum",c)
            else :
                print("e is maximum",e)
        else : 
            if d > e :
                print("d is maximum",d)
            else : 
                print("e is maximum",e)