class SystemCommandExecution(Exception):
    def __init__(self, reason:str = 'Check your command. Not successful result.'):
        self.reason = reason
        super().__init__(self.reason)