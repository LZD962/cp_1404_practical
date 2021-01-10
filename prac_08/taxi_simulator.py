from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    total_trip_cost = 0
    taxi = None

    print("Let's drive!")
    while True:
        s = menu(total_trip_cost)
        if s == "d":
            if taxi is not None:
                taxi.start_fare()
                taxi.drive(float(input("Drive how far? ")))
                trip_cost = taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(taxi.name, trip_cost))
                total_trip_cost += trip_cost
            else:
                print("Please choose a taxi first")
        elif s == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi = taxis[int(input("Choose taxi: "))]
        elif s == "q":
            print("Total trip cost: ${:.2f}".format(total_trip_cost))
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            break
        else:
            print("Invalid option")


def menu(total_trip_cost):
    if total_trip_cost is not None:
        print("Bill to date: ${:.2f}".format(total_trip_cost))
    print("q)uit, c)hoose taxi, d)rive")
    return input(">>> ").lower()


main()
