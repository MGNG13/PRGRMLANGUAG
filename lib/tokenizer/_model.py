class NonFormattedLineToken():
    def __init__(self, _line:str, _splitted_line):
        self.line: str = _line
        self.splitted_line: list = _splitted_line

    def _getObj(self):
        return {
            "line": self.line,
            "splitted": self.splitted_line
        }