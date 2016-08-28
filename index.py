import sys
import os

def main(filepath):
    """
        this is where your code goes...

        filename_without_ext is useful so you can
        save a new file with a new extention
    """

    filename_without_ext = os.path.splitext(filepath)[0]

if __name__ == "__main__":
    main(sys.argv[1])
