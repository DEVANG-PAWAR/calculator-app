a=float(input("Enter number"))
b=input("Enter operator")
c=float(input("enter number"))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    if c!=0:
         print==(a/c)
    else:
     print("cannot divide by zero")
else:
  print("fail")