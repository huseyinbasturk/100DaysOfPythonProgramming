print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
bill_with_tip = bill + bill / 100 * tip

bill_per_person = round(bill_with_tip / num_people,2)
final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_bill}")