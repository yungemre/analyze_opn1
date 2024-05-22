from .parse import parameters
from .analyze import read_parameters


def main():

    args = parameters()

    read_parameters(args)


if __name__ == '__main__':
    main()