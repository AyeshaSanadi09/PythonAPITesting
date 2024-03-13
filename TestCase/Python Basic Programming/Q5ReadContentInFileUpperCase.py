f = open("TestCase\\Python Basic Programming\\file4.txt", "r")
f2 = open("TestCase\\Python Basic Programming\\file5.txt", "w")

data = f.readline()
while(data):
    f2.write(data.upper())
    data = f.readline()