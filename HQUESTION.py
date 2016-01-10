l = [] #declares the variable
val = 0  #initialize variable

while (val!='h'): #terminate condition
    val = raw_input('Enter the value')
    l.append(val) #append values

t = tuple(l) #list to tuple

print t #print tuple
print l #print list
