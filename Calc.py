import sys
p=3.14159265359
q=2*p
a=float(input("Enter the first number--> "))
b=float(input("Enter the second number(if any,else 0)--> "))
c=int(input('''Enter
               1 for addition
               2 to subtract second number from first number
               3 to subtract first number from second number
               4 for multiplication
               5 for first number divided by second number
               6 for second number divided by first number
               7 for first number raised to second number 
               8 for second number raised to first number 
               9 for sin(first number)
               10 for cos(first number)
               11 for tan(first number)-->'''))
if c>=9:
    if a>0:
        if a>q:
            r=int(a/q)
            a=a-r*q
    else:
        z=-a 
        if z>q:
            r=int(z/q)
            a=-(z-r*q)
#undefined:
if c==11:
    if a%(1.57)==0:
        b=a/(1.57)
        if b%2!=0:
            print("Undefined")
            sys.exit()
if c==1:
    d = a+b
    print(d)
if c==2:
    d = a-b
    print(d)
if c==3:
    d = b-a
    print(d)
if c==4:
    d = a*b
    print(d)
if c==5:
    d = a/b
    print(d)
if c==6:
    d = b/a
    print(d)
if c==7:
    d = a**b
    print(d)
if c==8:
    d = b**a
    print(d)
if c==9:
    d=0
    for i in range(1,51):
        f=2*i-1
        if i%2==0:
            h=1
            for g in range (f,0,-1):
                h=h*g
            d=d-((a)**(f))/h
           
        else:
            h=1
            for g in range (f,0,-1):
                h=h*g
            d=d+((a)**(f))/h
    print(d)
if c==10:
    d=1
    for i in range(1,51):
        f=2*i
        if i%2==0:
            h=1
            for g in range (f,0,-1):
                h=h*g
            d=d+((a)**(f))/h       
        else:
            h=1
            for g in range (f,0,-1):
                h=h*g
            d=d-((a)**(f))/h
    print(d)
if c==11:
    s=1#cos
    for i in range(1,51):
        f=2*i
        if i%2==0:
            h=1
            for g in range (f,0,-1):
                h=h*g
            s=s+((a)**(f))/h       
        else:
            h=1
            for g in range (f,0,-1):
                h=h*g
            s=s-((a)**(f))/h
    cos=s
    #now sin a = (a**(2n-1))/(2n-1)!
    #sinx= x- x^3/3!+ x^5/5!-...
    m=0#sin
    for i in range(1,51):
        f=2*i-1
        if i%2==0:
            h=1
            for g in range (f,0,-1):
                h=h*g
            m=m-((a)**(f))/h
           
        else:
            h=1
            for g in range (f,0,-1):
                h=h*g
            m=m+((a)**(f))/h
    sin=m
    tan=(sin)/(cos)
    print(tan)


    

        
    
               
