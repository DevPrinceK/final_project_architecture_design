'''A Python program to find 
    the average of all even numbers 
    between one and 10000
'''
def find_average_of_even_nums(start=1, limit=10000):
    even_nums_count = 0
    total = 0
    for num in range(start, limit):
        if num % 2 == 0:
            even_nums_count += 1
            total += num
    return total / even_nums_count

# This calls the function to perform the the computations
find_average_of_even_nums()