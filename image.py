import urllib
f = open('logo.png','wb')
f.write(urllib.urlib('abc.com/1.png').read())
f.close()
