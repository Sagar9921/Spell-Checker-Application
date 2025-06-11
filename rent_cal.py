rent =  int(input("Enter the total rent of your property = "))
food = int(input("Enter the Amount of Food Ordered = "))
electricity = int(input("Enter the Electricity spend = "))
charge_per_unit = int(input("Enter the Charges per unit  = "))
persone = int(input("Enter the total number of total persone living = "))

total_bill = electricity * charge_per_unit
output = (food + rent + total_bill) // persone


print("Each persone will pay amount of", output ,"Rs")

