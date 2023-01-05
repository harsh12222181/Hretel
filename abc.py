a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    if b>=c:
        print("min",b)
    else:
        print("min",b)
        print("max",a)
    if b>=c:
        print("min",a)
    else:
        print("min",c)
    print("max",b)
    if c>=a and c>=b:
        print("min",b)
    else:
        print("min",a)
    print("max",c)