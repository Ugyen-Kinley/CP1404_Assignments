print("For part (a): Odd numbers between 1 and 20")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("For part (b): Count in 10s from 0 to 100")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("For part (c): Count down from 20 to 1")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("For part (d): Print n stars on one line")
the_number_of_stars = int(input("Number of stars: "))
for i in range(the_number_of_stars):
    print('*', end='')
print()

print("For part (e): Print n lines of increasing stars")
for i in range(1, the_number_of_stars + 1):
    print('*' * i)
