### PROBLEM 4

#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit
#                       numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


a = 100
b = 100
c = 0
palindromi = []

while a < 1000 and b < 1000:
    while a < 1000 and b < 1000:
        c = a * b
        cString = str(c)    #casted to str to use the positional checks
    
        
        
        if cString[0] == cString[-1] and cString[1] == cString[-2] and cString[2] == cString[-3]:
            #print("A=",a,"B=",b,"C=",c, "Lunghezza=",lungC)
            a +=1
            palindromi.append(c)
        else:
            a +=1
        
    b +=1
    a= 100

palindromi.sort()   #it contains every palindrome found
print(palindromi[-1])   #prints only the largest one
    
