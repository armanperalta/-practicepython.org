"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
#Solution 1
num = int(input('Enter a number: '))
type = num % 2
type2 = num % 4
if type == 0 or type2 == 0:
    print('Even number!')
    if type2 == 0:
        print('Also multiple of 4!')
else:
    print('Odd number!')

#Solution 2
num = int(input('Enter a number to check: '))
check = int(input('Enter a number to divide by: '))
type = num % check
if type == 0:
    print(check, 'is multiple of', num)
else:
    print(check, 'is NOT multiple of', num)