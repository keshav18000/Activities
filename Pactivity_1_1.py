'''
Problem 1:
Suppose you are buying something online on amazon.com 
On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.
Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
'''
def discounted_price(amount, prime_member):
    prime_discount = 0.15
    black_friday_discount = 0.08
    if prime_member:
        amount *= (1 - prime_discount)
    amount *= (1 - black_friday_discount)
    return amount

amount = 4500
is_prime_member = True

discounted_amount = discounted_price(amount, is_prime_member)
print(discounted_amount)