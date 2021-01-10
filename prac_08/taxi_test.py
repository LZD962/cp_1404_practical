from prac_08.taxi import Taxi


def main():
    t = Taxi("Prius 1", 100, 1.23)
    t.drive(40)
    print(t)
    t.start_fare()
    t.drive(100)
    print(t)


main()
