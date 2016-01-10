X = int(input('Enter the value of X :'))    #first Variable
Y = int(input('Enter the value of Y :'))    #Second Variable
#Choose the operator
print "1 for addition"
print "2 for subraction"
print "3 for multiplication"
print "4 for division"

a = int(input('Enter your operator:'))

if a == 1:
    print X+Y   #Addition
elif a==2:
    print X-Y   #Subraction
elif a==3:
    print X*Y   #Multiplaction
elif a==4:
    print X/Y   #Division
else:
    print "invalid selection"

#end of the programe
