total = 0
Number = int(input("Number Of Items:"))
while Number < 0:
    print("Invalid Number Of Items")
    Number = int(input("Number Of Items:"))
for i in range(Number):
    price = float(input("Price Of Item:"))
    total += price
if total > 100:
    total *= 0.9
print("Total price for", Number, "items is $", total, sep=" ")
