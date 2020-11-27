score = float(input("Enter score: $"))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
if 100 > score >= 50:
    print("Pass")
if 100 > score >= 90:
    print("Excellent")
if score < 50:
    print("Bad")
