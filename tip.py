print("Welcome to the Tip Calculator")
bill = float(input("What is your total bill? "))
tip_perc = int(input("How much tip would you like to give? 10, 12, or 15 percent? "))
split = int(input("How many people to split the bill? "))

tip = (bill * (tip_perc/100))

final_bill = print(f"Each person should be paying {round((bill + tip) / split, 2)}")