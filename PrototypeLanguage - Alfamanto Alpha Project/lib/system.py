import sys


def get_terminal_arguments() -> list:
    """
    This function returns a list of arguments without empty args.
    Example:
        python main.py arg1 "   " arg2
        returns -> ["arg1", "arg2"]
    """
    return [argument for argument in sys.argv[1:] if argument.strip()]
