class TokenizerInvalidInstance(Exception):
    def __init__(self, reason:str = 'Invalid tokenizer instance.'):
        self.reason = reason
        super().__init__(self.reason)