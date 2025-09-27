for i in range(1, 21, 2):
    print(i, end=' ')
print()
"""
Part A: count in 10s from 0 to 100
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()
"""
Part B: count down from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()
"""
Part C: print a number of stars
"""
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()
"""
Part D: print lines of increasing stars
"""
for i in range(0, number_of_stars + 1):
    print('*'*i) # prints number_of_stars increasing by one for the amount of lines (i) entered
print()