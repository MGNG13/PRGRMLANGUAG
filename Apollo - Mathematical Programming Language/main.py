# Python Imports.
from sys import argv

# CONSTANTS.
global MAX_INPUT_SIZE
MAX_INPUT_SIZE = 1


# This class makes some validations in all code processing.
class Validator():
    def is_file(filename: str) -> bool:
        try:
            open(filename, 'r').encoding
            return True
        except Exception:
            return False

# Main class about apollo lang.
class ApolloLang():
    class Keywords():
        class THEN():
            def __init__(self):
                # before internal parsing.
                self.token_name = 'THEN'

        class PROCEDURE():
            def __init__(self, _PlainLinesTokens: list):
                # before internal parsing.
                self.token_name = 'PROCEDURE'
                self.token_plain_lines_tokens = _PlainLinesTokens
                # to parse in internal parsing.
                self.token_lines_tokens = None
                self.token_lines_length = 0
                self.token_tokens_length = 0
                self._doInternalParsing(self)

            def _doInternalParsing(self):
                pass

        class ADD():
            def __init__(self, _PlainLinesTokens: list):
                # before internal parsing.
                self.token_name = 'ADD'
                self.token_plain_lines_tokens = _PlainLinesTokens
                # to parse in internal parsing.
                self.token_arguments = None
                self.token_method_finalization = None
                self._doInternalParsing(self)

            def _doInternalParsing(self):
                pass


# This root class only saves the state from each token as instruction.
class Tokens():
    class LineToken():
        def __init__(self, Line: str):
            self.Line: str = Line

        def getLine(self) -> None or str:
            return self.Line

        def parseTokens() -> None or list:
            try:
                pass
            except Exception:
                pass

# This class makes an parsing of each line and each token.
class Parser():
    def EmptyTokenizer(apollo_code: str) -> None or list:
        try:
            LinesToken: list = []
            for line in apollo_code.split('\n'):
                line_token = Tokens.LineToken(line)
                line_token.parseTokens()
                LinesToken.append(line_token)
            return LinesToken
        except Exception:
            return None


# Main thread running validation.
if __name__ == '__main__':
    # Arguments to interpretter.
    ARGUMENTS = argv[1:]

    # Some validation.
    if len(argv) <= 1 or len(argv) > MAX_INPUT_SIZE + 1:
        print('Check your input values. Invalid data input.')
    else:
        if not Validator.is_file(ARGUMENTS[0]):
            print('Check your input file. Not valid Apollo File.')
        else:
            # Read code.
            apollo_code_file = open(ARGUMENTS[0], 'r')
            apollo_code_content = apollo_code_file.read()
            apollo_code_file.close()

            # Parsing.
            print(Parser.EmptyTokenizer(apollo_code_content))