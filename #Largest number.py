#Largest number
#A program to find the largest of 3 numbers
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
num3=int(input("Please enter the third number: "))
if (num1 > num2 and num1 > num3):
    largest_number=num1
    print("The largest of the three numbers is:",num1)
elif (num2 > num1 and num2 > num3):
    largest_number=num2
    print("The largest of the three numbers is:",num2)
else:
    largest_number=num3
    print("The largest of the three numbers is:",num3)    