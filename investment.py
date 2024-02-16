starting_balance=float(input("Enter the investment amount: "))
years=int(input("Enter the number of years: "))
rate=float(input("Enter the rate as a %: "))/100
total_interest=0.0
print("Year\tStarting Balance\tInterest\tEnding Balance")
for i in range(1,years+1):
    interest=starting_balance*rate
    ending_balance=starting_balance+interest
    print(i,"\t","%0.2f"%starting_balance,"\t\t","%0.2f"%interest,"\t","%0.2f"%ending_balance)
    total_interest+=interest
    starting_balance=ending_balance
print("Ending balance: ","%0.2f"%ending_balance)
print("Total interest earned: ","%0.2f"%total_interest)
