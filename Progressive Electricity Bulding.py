units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.5 + 50
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5 + 50
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4 + 50

if units >= 0:
    print("Total Electricity Bill:", bill)