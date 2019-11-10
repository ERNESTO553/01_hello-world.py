def fib (n):
    a = 0
    b = 1
    while a<n:
        print(a , end='\n')
        c=a+b
        a=b
        b=c
        print ()
fib (100)
##a,b=b, a+b
