dm = open("demo.txt","w")
dm.write("this is my demo file line\n")
dm.write("this is my demo second line\n")
dm.write("this is the demo third line\n")
dm.write("this is the last one\n")
dm.close()

dm = open("demo.txt","r")
dmd = dm.read()
print (dmd)
dm.close()

dm = open("demo.txt","a")
the = ["this added now\n","and this also\n"]
dm.writelines(the)

dm.close()
dm = open("demo.txt","r")
dmd = dm.read()
print (dmd)
dm.close()


dm = open("demo.txt","w")
try:
    dm.write("python is awsome\n")
    dm.write("python is good\n")
except Exception, e:
    print 'an error occured'
dm.close()

dm = open("demo.txt","r")
dmd = dm.read()
print (dmd)
dm.close()
