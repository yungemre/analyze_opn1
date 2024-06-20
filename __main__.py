from .parse import parameters
from .analyze import read_parameters


def main():

    # Command line parameters
    args = parameters()

    # Reads paramaters and analyzes them (analyze.py)
    read_parameters(args)


if __name__ == '__main__':
    main()