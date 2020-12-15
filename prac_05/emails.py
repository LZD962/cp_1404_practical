emails = {}
e = input("Email: ")
while e != "":
    name = e.split("@")[0].replace(".", " ").title()
    check = input("Is your name {}? (Y/n) ".format(name))
    if check.lower() != "y" and check != "":
        name = input("Name: ")
    emails[e] = name
    e = input("Email: ")

for e, name in emails.items():
    print("{} ({})".format(name, e))
