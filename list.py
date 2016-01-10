l = [1,2,3,4,5]
print l
print len(l)
print l[0]
print l[4]

for i in l:
    print i



l = [1,2,3,4,5]
l.append(2) #add values to last
l[0] = 'hello' edit value on 0
l.insert(2,'abc') #insert value at
l.remove('abc') #removes value
del l[0] #removes position
print l #print list l
print l.index('abc') #print position 
