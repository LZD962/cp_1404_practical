import os


def main():
    ets = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        ets[filename.split('.')[-1]] = None

    for e in ets:
        cate = input("What category would you like to sort {} files into? ".format(e))
        try:
            os.mkdir(e)
        except FileExistsError:
            pass
        ets[e] = cate

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        e = filename.split('.')[-1]
        os.rename(filename, "{}/{}".format(ets[e], filename))


main()