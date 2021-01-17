import os
import shutil


def main():
    try:
        os.chdir("FilesToSort")
    except FileExistsError:
        pass

    ets = set()
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        ets.add(filename.split('.')[-1])

    for e in ets:
        try:
            os.mkdir(e)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        shutil.move(filename, "{}/{}".format(filename.split('.')[-1], filename))


main()
