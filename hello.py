a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=int(input("Enter another number"))
if(a>b and a>c):
    print(f"{a} is the greatest")
elif(b>c):
    print(f"{b} is the greatest")

else:
    print("{} is greatest".format(c))