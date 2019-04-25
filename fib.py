a,b=1,1
print("fibonacci.of( 1 )=",a)
print("fibonacci.of( 2 )=",b)
i=3
while i<=200:
    a,b=b,a+b
    print("fibonacci.of(",i,")=",b)
    i=i+1


