"""
CP1404/CP5632 - Practical
Temperature conversions
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = f_to_c(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
            print(MENU)
        choice = input(">>> ").upper()
        print("Thank you.")


def c_to_f(celsius):
    return celsius * 9.0 / 5 + 32


def f_to_c(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9


main()
