def readEvenAndOddLines(f1):
    oddData = f1.readline()
    evenData = f1.readline()
    while(evenData and oddData):
        print("Odd Line: "+oddData)
        print("Even Line: "+evenData)
        oddData = f1.readline()
        evenData = f1.readline()


f1 = open("TestCase\\Python Basic Programming\\file3.txt", "r")
readEvenAndOddLines(f1)
f1.close()