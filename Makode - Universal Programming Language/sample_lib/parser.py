# main lib.
from lib._exceptions.parser_exception import TokenizerInvalidInstance

# manow lib.
from lib.tokenizer import Tokenizer


class Parser():
    def __init__(self, tokenizer: Tokenizer=None):
        if tokenizer is None:
            raise TokenizerInvalidInstance()
        self.tokenizer = tokenizer
        self._parseTokens(self)

    def _parseTokens(self):
        pass