print("Enter the length of three side of the triangle:")
a,b,c=int(input()),int(input()),int(input())
if a==b and a==b and a==c:
    print("triangle is equilateral")
elif a==b or b==c or a==c:
    print("triangle is a isoscale")
else:
    print("triangle is a scalene")