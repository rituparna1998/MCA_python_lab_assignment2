m1=float(input("Enter marks of subject 1:"))
m2=float(input("Enter marks of subject 2:"))
m3=float(input("Enter marks of subject 3:"))
m4=float(input("Enter marks of subject 4:"))

average=(m1+m2+m3+m4)/4
print(average)
if(average>=40):
    print("Congratulation You have Passed")
else:
    print("Sorry You Failed")