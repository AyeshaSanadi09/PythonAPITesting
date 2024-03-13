f = open("TestCase\\Python Basic Programming\\file3.txt", "r")

data = f.readline()
while(data):
    if("error" in data):
        pass
    else:
        print(data, end=" ")
    data = f.readline()