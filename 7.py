print("Enter three numbers:")
n1,n2,n3=int(input()), int(input()), int(input())
if(n1<n2<n3 or n3<n2<n1):
    print(n2,"is the second smallest")       
elif(n2<n3<n1 or n1<n3<n2):
    print(n3,"is the second smallest")
else:
    print(n1,"is the second smallest")