f = open("TestCase\\Python Basic Programming\\file3.txt", "r")
f2 = open("TestCase\\Python Basic Programming\\file4.txt", "w")

data = f.readline()
while(data):
    if("error" in data):
        f2.write(data)
    else:
        pass
    data = f.readline()