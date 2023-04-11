'''
Problem Statement- II
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2
'''

n = 28
divisors_sum = sum([i for i in range(1, n) if n % i == 0])

if divisors_sum > n:
    print(n, "is an abundant number")
elif divisors_sum < n:
    print(n, "is a deficient number")
else:
    print(n, "is a perfect number")
