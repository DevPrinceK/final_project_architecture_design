'''
A Python Program to sum all prime numbers in a given range
'''

def find_sum_of_prime_nums(limit=20):
    sum = 0
    if limit > 1:
        for num in range(2, limit):
            check = False
            for i in range(2, num):
                if num % i == 0:
                    # it is not a prime.
                    check = False
                    break
                else:
                    check = True
            if check:
                sum += num
        return sum
                
    else:
        return "Number must be greater than 1"