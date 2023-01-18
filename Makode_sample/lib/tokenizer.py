class Tokenizer():
    def __init__(self, plain_text_code: str=None):
        self.plain_text_code = plain_text_code
        self.tokenized = []
        self._parseTokens(self)

    def _parseTokens(self):
        for _splitted_newlines in self.plain_text_code.split('\n'):
            _splitted_newlines = _splitted_newlines.split(' ')
            self.tokenized.append(_splitted_newlines)
        return self.tokenized

    def getTokens(self):
        return self.tokenized