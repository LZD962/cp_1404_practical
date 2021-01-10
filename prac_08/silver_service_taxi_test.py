from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    t = SilverServiceTaxi("Car 1", 100, 30)
    print(t.get_fare())
    t.drive(40)
    print(t)
    t.drive(100)
    print(t)
    print(t.get_fare())

main()
