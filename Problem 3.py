## PROBLEM 3
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


n = 600851475143
primo = 2

while primo <= n:
    if n % primo ==0:
        print(primo)    #the prime factors
        n = n/primo
        primo += 1
    else:
        primo += 1

print("Il risultato è =", primo)    #the largest one
