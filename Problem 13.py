### PROBLEM 13
#Work out the first ten digits of the sum of the following
#           one-hundred 50-digit numbers. (in "Problem 13.txt")

filein = open("Problem 13.txt","r",encoding = "UTF-8")

fileNum = 0
for riga in filein:
    fileNum += int(riga)
    #print(riga)
    
print(fileNum)
fileNum = str(fileNum)
print("Le prime 10 cifre sono", fileNum[:10])
