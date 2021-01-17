import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        for f in filenames:
            old_name = os.path.join(directory_name, f)
            new_name = os.path.join(directory_name, get_fixed_filename(f))
            os.rename(old_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    return filename.replace(" ", "_").lower()


main()
