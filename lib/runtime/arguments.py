from lib.exceptions.transpilation import TranspilationArguments, TranspilationEngineUncaught
from sys import argv


def get_arguments(min_args: int=None, max_args: int=None):
    try:
        _arguments = argv[1:]
        if min_args == None or max_args == None:
            raise TranspilationEngineUncaught()
        if len(_arguments) == 0:
            raise TranspilationArguments('No file provided.')
        if len(_arguments) > max_args:
            raise TranspilationEngineUncaught()
        return _arguments
    except Exception:
        raise TranspilationArguments('Empty args.')