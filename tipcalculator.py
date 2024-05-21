// Tip Calculator 

bill = float(input("enter the bill"))
tip = int (input("How much tip do you want to give ? 10,12,15?"))
people= int (input("How many people to split bill?"))
bill_with_tip= tip/100*bill+bill
bill_per_person=bill_with_tip/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay {final_amount}")