f1 = open("TestCase\\Python Basic Programming\\file1.txt", "r")
data1 = f1.readlines()
f1.close()

f2 = open("TestCase\\Python Basic Programming\\file2.txt", "r")
data2 = f2.readlines()
f2.close()


f3 = open("TestCase\\Python Basic Programming\\file3.txt", "+a")
f3.writelines(data1)
f3.writelines(data2)
f3.close()
