# runtime main libs.
from lib.runtime.arguments import get_arguments

# required.
from lib.tokenizer.tokenizer import Tokenizer


if __name__ == '__main__':
    # args.
    _arguments = get_arguments(1, 1)
    _file_name = _arguments[0]

    with open(_file_name, 'r') as _file:
        # read file
        _file_content = _file.read()
        # convert lines as tokens.
        _tokenizer = Tokenizer(_file_content)
