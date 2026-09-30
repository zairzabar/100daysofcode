height = int(input("What's your heght in CMs? "))
weight = int(input("What's your weight in KGs? "))

hm = float(height) * 0.01

bmi = weight / hm ** 2

print(round(bmi, 2))