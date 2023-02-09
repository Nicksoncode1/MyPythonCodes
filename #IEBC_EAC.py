#IEBC_EAC
east_africa=['Kenyan' , 'Ugandan' , 'Tanzanian']
age=int(input("Please enter your age: "))
nationality=input("Please enter your Nationality: ").capitalize()
if(age >=18 and nationality in east_africa):
    print("Eligible to vote...")
else:
    print("Unfortunately NOT ALLOWED to vote!!!")    