# data=[]
# with open("sample.txt", "r") as f:
#     # print(len(f.readlines()))
#     for i in f.readlines():
#         data.append(i)
# print(data)


# f = open("sample.txt", "r")
# data = f.read()
# while data:
#     print(data)
#     data = f.read()
# f.close()


# f = open("sample.txt", "a")
# f.write("hii i am aswdnji  edguiheuihweied")
# f.close()


# f = open("sample.txt", "r")
# print(f.readlines())
# f.close()

# with open("sample.txt") as f:
#     print(f.readline())
#     f.close()

# import os
# os.remove("sample.txt")


# tell = return the cursor position
# seek = set the cursor position

f = open("sample.txt", "r")
print(f.tell()) 
f.readline()
print(f.tell()) 
f.seek(15)
print(f.tell()) 
