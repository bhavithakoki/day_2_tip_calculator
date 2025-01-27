# DAY_2 PROJECT IS : A TIP CALCULATOR  BY USING PYTHON
print("WELCOME TO THE TIP CALCULATOR!")
#taking input from user
total_bill=float(input("what was the total bill?\n$"))
tip=int(input("how much tip would you like to give? 10,12or 15?\n"))
people=int(input("how many people to split the bill?\n"))
tip_in_amount=(tip/100)*total_bill+total_bill
each_bill=tip_in_amount/people
print(f" Each person should pay:${each_bill}")