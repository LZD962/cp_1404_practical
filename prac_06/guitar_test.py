from prac_06.guitar import Guitar

if __name__ == '__main__':
    g1 = Guitar("Gibson L-5 CES", 1922, 50)
    g2 = Guitar("Another Guitar", 2013, 100)

    print("{} get_age() - Expected {}. Got {}".format(g1.name, 98, g1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(g2.name, 7, g2.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(g1.name, True, g1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(g2.name, False, g2.is_vintage()))
