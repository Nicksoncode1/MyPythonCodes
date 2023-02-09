#Discount
purchase=int(input("Please enter the value of your purchase:"))
if (purchase > 1000):
    discount=0.05 * purchase
    print("Discount is:" ,discount)
    Amount_Payable=purchase-discount
    print("Ammount to be paid minus the discount:",Amount_Payable)
else:
    print("No Discount!!!")    
