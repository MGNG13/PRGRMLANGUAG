class TokenizerParseUncaught():
    def __init__(self, reason:str = 'Uncaught token.'):
        self.reason = reason
        super().__init__(self.reason)