a = int(input("enter a maths marks:"))
b = int(input("enter a attendence :"))
c = input("enter a has_medical (yes/no):").lower()
has_medical = True
not_medical = False

if a < 0 or a > 100 :
    print("invalid marks")
else:
    if a  >= 40:
        if b >= 75 or  c == "yes":
           if a >= 90:
               print("grade a")
           elif a >=75:
                print("grade b")
           elif a >= 60:
                print("grade c")
           else :
               print("grade d")
        else :
              print("not eligible due to low attendence or not has medical certi")   
    else :
       print("failed") 

     