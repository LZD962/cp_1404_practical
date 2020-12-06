import random


def main():
    score = float(input("Enter score: $"))
    result = get_result(score)
    print(result)

    random_num = random.random()
    result = get_result(random_num)
    print(result)


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
