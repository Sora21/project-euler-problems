#The sum of the squares of the first ten natural numbers is,

        #1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,

        #(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural
#numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sum.




n = 0
sommq = 0   #Somma dei quadrati
qsomm = 0   #Quadrato della somma

# Somma dei quadrati
while n != 101:
    sommq += n ** 2
    #print("N=",n,"Sommq=",sommq)
    n += 1



n = 0
# Quadrato della somma
while n != 101:
    qsomm += n
    n += 1
qsomm = qsomm**2
#print("Qsomm=",qsomm)
    
fine = qsomm - sommq
print(fine)
