def isNumber(value: any) -> bool:
    try:
        """
        Convert to string, remove all blank spaces and convert to integer.
        """
        int(str(value).replace(" ", ""))
        return True
    except Exception:
        return False
        