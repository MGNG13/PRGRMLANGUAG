from lib.tokenizer.tokens import INTERPRETER_TOKENS, TRANSPILER_TOKENS
from lib.tokenizer._model import NonFormattedLineToken


class Tokenizer():
    def __init__(self, plain_text_code: str=None):
        # Initialize Tokenizer configuration.
        self.plain_text_code: str = plain_text_code
        self.tokens: list = []
        self.lines: list = []
        # Initialize tokenizer.
        self._parseEachLineToJsonReadable()
        self._parseTokens()
    
    """
    Second Stage. self.lines [NonFormattedLineToken] -> append -> self.tokens
    """
    def _parseTokens(self):
        if len(self.lines) == 0:
            raise Exception('No tokens found.')

        def _parseInterpreterTokens(_line:str):
            for _interpreter_token in INTERPRETER_TOKENS:
                for _line_splitted in _line['splitted']:
                    if _line_splitted.__contains__(_interpreter_token().getPattern()):
                        print(_line_splitted)

        #_parseInterpreterTokens(self.lines)
        print(self.lines)
        # def parseMultipleLinesTokens
        #for _line in self.lines:
            #print(_line)

    """
    First Stage. plain-text to 'self.lines' -> NonFormattedLineToken
    """
    def _parseEachLineToJsonReadable(self):
        # Index of read file.
        _index_file: int = 0
        # Split newlines.
        for _line in self.plain_text_code.split('\n'):
            # Line number with blackspace splitted lines.
            self.lines.append(NonFormattedLineToken(
                _index_file,
                list(filter(lambda token: (token != ''), _line.split(' ')))
            ))
            _index_file += 1
        return self.lines

    """
    GETTER METHODS;
    """
    def getLines(self):
        return self.lines

    def getTokens(self):
        return self.tokens
