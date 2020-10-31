def gcd(x,y):
     if(y==0):
          return x
     else:
          return gcd(y,x%y)
x=int(input("Enter the First No.:  "))
y=int(input("Enter the Second No.: "))
GCD=gcd(x,y)
print(GCD)
