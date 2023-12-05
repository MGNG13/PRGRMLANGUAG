class TranspilationArguments(Exception):
    def __init__(self, reason:str = 'There are no valid arguments.'):
        self.reason = reason
        super().__init__(self.reason)

class TranspilationEngineUncaught(Exception):
    def __init__(self, reason:str = 'Transpiler internal exception.'):
        self.reason = reason
        super().__init__(self.reason)