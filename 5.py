n=input("Enter a number:")
chk=n.isdigit()
if chk==True:
    length=len(n)
    if(length==2):
        print("the given number is two digit number")
    else:
        print("the given number is not two digit")
        
else:
    print("Enter a valid number")