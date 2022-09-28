"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    number = 2
    while count < number_of_primes:
         prime = True
         for i in range(2, number):
             if number % i == 0:
                 prime = False
                 break
         if prime:
             list.append(number)
             count += 1
         number += 1
    return list
