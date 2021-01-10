from prac_08.unreliable_car import UnreliableCar


def main():
    t = UnreliableCar("Car 1", 100, 30)
    t.drive(40)
    print(t)
    t.drive(100)
    print(t)


main()
