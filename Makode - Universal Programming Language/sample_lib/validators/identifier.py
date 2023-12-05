def is_valid_identifier(identifier: str or any=None):
    if not isinstance(identifier, str):
        return False
    if identifier.isnumeric():
        return False
    if not identifier.isidentifier():
        return False
    return True