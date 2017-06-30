### PROBLEM 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#   we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


maxLimit = 999



def findMultiples(num, currMultiplier, totalMultiplesSum):
    currNum = num
    while num * currMultiplier <= maxLimit:
        
        currNum = num * currMultiplier
        currMultiplier += 1
        totalMultiplesSum += currNum
        #print(num, totalMultiplesSum)
    return totalMultiplesSum


result = (findMultiples(3, 1, 0) + findMultiples(5, 1, 0)) - findMultiples(15, 1, 0)
print("Il risultato è =", result)


#To find the solution I calculated the sum of the multiples of 3, plus the same
#thing for 5, subtracting the sum of the multiples of 15 to take away the
#already shared multiples between the two
