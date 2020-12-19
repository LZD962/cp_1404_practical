from prac_06.guitar import Guitar

if __name__ == '__main__':
    gs = []
    gs.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    gs.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    name = input("Name: ")
    if name != "":
        year = input("Year: ")
        cost = float(input("Cost: $"))
        new_g = Guitar(name, year, cost)
        print(new_g, "added.")
        gs.append(new_g)
        name = input("Name: ")

    print("... snip ...")

    print("These are my guitars:")
    for i, g in enumerate(gs):
        num = i + 1
        v = ""
        if g.is_vintage():
            v = "(vintage)"
        print("Guitar {}: {} ({}), worth ${:,.2f} {}".format(num, g.name, g.year, g.cost, v))
