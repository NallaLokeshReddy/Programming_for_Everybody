# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.

hrs = input("Enter the number of Hours worked: ")
rt = input ('Enter the require rate per hour: ')
hours = float(hrs)
rate = float(rt)
if hours < 40 :
    print(hours*rate)
else :
    print(40*rate + (hours - 40)*rate*1.5)
