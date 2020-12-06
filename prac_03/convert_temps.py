def main():
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_output.txt", "w")

    for t in input_file:
        f = float(t)
        c = f_to_c(f)
        output_file.write("{}\n".format(c))

    input_file.close()
    output_file.close()


def c_to_f(celsius):
    return celsius * 9.0 / 5 + 32


def f_to_c(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9


main()
