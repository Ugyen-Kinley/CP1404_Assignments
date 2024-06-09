import random

print(random.randint(5, 20))
# line 1
# Possible outputs observed are: 7, 13, 19, etc.
# Smallest possible number is: 5
# Largest possible number is: 20

print(random.randrange(3, 10, 2))
# line 2
# Possible outputs observed are: 3, 5, 7, 9
# Smallest possible number is: 3
# Largest possible number is: 9
# Line 2 could not have produced a 4 because the step is 2, starting from 3.

print(random.uniform(2.5, 5.5))
# line 3
# Possible outputs observed are: 3.47, 4.82, 2.76, etc.
# Smallest possible number is: 2.5
# Largest possible number is: 5.5

# The code to produce a random number between 1 and 100 inclusive is
print(random.randint(1, 100))
