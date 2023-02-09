#Bonus
sal=int(input("Please enter your salary: "))
YearOfService=int(input("Please enter your years of service: "))
if(YearOfService > 10 ):
    bonus=0.1 * sal
    print("Your bonus is: ",bonus)
    Net_salary=sal+bonus
    print("Your net salary is: ",Net_salary)
elif(YearOfService >= 6 and YearOfService <= 10 ):
    bonus=0.08 * sal
    print("Your bonus is: ",bonus)
    Net_salary=sal+bonus
    print("Your net salary is: ",Net_salary)
else:
    bonus=0.05 * sal
    print("Your bonus is: ",bonus)
    Net_salary=sal+bonus
    print("Your net salary is: ",Net_salary)    