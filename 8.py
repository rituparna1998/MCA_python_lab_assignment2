print("Enter the marks of five subjects:")
m1, m2, m3, m4, m5=int(input()), int(input()), int(input()), int(input()), int(input())
average=(m1+m2+m3+m4+m5)/5
if(average>=90):
    print("Grade is O")
elif(90>average>=80):
    print("Grade is E")
elif(80>average>=70):
    print("Grade is A")
else:
    print("Grade is B")
