#IEBC
age=int(input("Please enter your age: "))
nationality=input("Please enter your Nationality: ").capitalize()
if(age >= 18 and nationality == 'Kenyan'):
    print("Eligible to vote!!!")
else:
    print("NOT ALLOWED to vote!!!")    
