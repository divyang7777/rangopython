def printfunc():
    print 'hello'

def calfunc(a,b):
    c = a+b
    return c

def deffunc(a,b,c=5):
    return a+b+c

printfunc()
print calfunc(2,4)
print deffunc(2,4)
