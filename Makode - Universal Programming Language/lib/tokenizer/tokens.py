from lib.tokens.interpreter import _code, _system, _file, _directory
from lib.tokens.transpiler import _function, _println, _returnup, _transpilation_language, _variable


INTERPRETER_TOKENS: list = [
    _code.InterpreterTokenCode,
    _file.InterpreterTokenFile,
    _system.InterpreterTokenSystem,
    _directory.InterpreterTokenDirectory
]

TRANSPILER_TOKENS: list = [
    _transpilation_language.TranspilerTokenTranspilationLanguage,
    _variable.TranspilerTokenVariable,
    _function.TranspilerTokenFunction,
    _println.TranspilerTokenPrintln,
    _returnup.TranspilerTokenReturnup
]