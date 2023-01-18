from lib._exceptions.transpilation_exception import TranspilationArguments, TranspilationEngineUncaught
from sys import argv

def _get_arguments(min_args: int=None, max_args: int=None):
    _arguments = argv[1:]
    if min_args == None or max_args == None:
        raise TranspilationEngineUncaught()
    if len(_arguments) == min_args:
        raise TranspilationArguments('No files to transpile.')
    if len(_arguments) > max_args:
        raise TranspilationArguments('This transpiler only accepts 2 arguments at a time.')
    for i in range(0, len(_arguments)):
        if _arguments[i] == None or _arguments[i] == '':
            raise TranspilationArguments('Empty args.')
    return _arguments
