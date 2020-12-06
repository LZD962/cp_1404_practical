import random


def main():
    score_num = int(input("Enter score number: "))
    output_file = open("results.txt", "w")

    for _ in range(score_num):
        random_num = random.randint(0, 101)
        result = get_result(random_num)
        output_file.write("{} is {}\n".format(random_num, result))

    output_file.close()

def get_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
    if 100 > score >= 50:
        return "Pass"
    if 100 > score >= 90:
        return "Excellent"
    if score < 50:
        return "Bad"


main()
