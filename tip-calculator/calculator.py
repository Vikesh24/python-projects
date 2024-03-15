""" A Simple Command line program to calculate and split the bill """

# Greeting the user
print("Hiya! Welcome to Tip Calculator")

# Getting the total bill from the user
total_bill = int(input("How much is your total bill(in rupees)? "))

# Getting the percentage of the tip the user wish to give
tip = int(input("What percentage of amount you wish to give as tip? 5, 10 or 20 "))

total_to_pay = total_bill * (tip/100) + total_bill

# Getting the user's choice to split the bill
split_choice = input("Do you wish to split the bill [yes/no]?")


# Getting the no. people to split the bill
if split_choice == "yes":
    no_of_parts = int(input("Please enter the no. people sharing the bill: "))
    total_per_person = total_to_pay / no_of_parts

else:
    total_per_person = total_to_pay

print("Bill Summary")
print(f"{"Total Bill(without tip):".ljust(40)}{total_bill}")
print(f"{"Tip percentage:".ljust(40)}{tip}")
if split_choice == "yes":
    print(f"{"Bill split with:".ljust(40)}{no_of_parts}")
else:
    print(f"{"Bill Split with:".ljust(40)}" + "None")
print(f"{"Amount to be paid per person:".ljust(40)}{total_per_person}")
