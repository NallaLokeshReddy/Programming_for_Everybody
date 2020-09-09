# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

smallest_no = None
while True:
    inp = input('Enter a number: ')
    if( inp.isdigit() ) :
        num = int(inp)
        if smallest_no is None:
            smallest_no = num
            largest_no = num
        elif num < smallest_no :
            smallest_no = num
        elif num > largest_no :
            largest_no = num
    else:
        if inp == 'done' or inp == 'Done' or inp == 'DONE' :
            break
        else:
            print('Please Enter a valid number')
            continue
print('Maximum is',largest_no)
print('Minimum is',smallest_no)
