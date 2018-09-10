import os

def isChar(char):
    cValue = ord(char)
    return (cValue > 47 and cValue <58 or cValue > 64 and cValue < 91 or cValue > 96 and cValue < 123)

fileNameOne = input()
fileNameTwo = input()

#fileNameOne = "republic.txt"
#fileNameTwo = "new_republic_v2.txt"

file = open(fileNameOne, 'r')
outFile = open(fileNameTwo, 'w')
fileText = file.readlines()
newFileText = ""

i = 0
j = 0
for line in fileText:
    j = 0
    while j < len(line) and ((i < 81 or line[j] != "\n" or ord(line[i]) != 0)):
        newFileText = newFileText + line[j]
        if(i == 80 ):
            newFileText = newFileText + "\n"
            i = 0
        else:
            i += 1
        j += 1

outFile.writelines(newFileText)
file.close()
outFile.close()
print("finished")

