def s2b(v, default=True):
    """
    Checks if a string can be converted to a boolean
    """
    if isinstance(v, bool):
        return v
    elif v.lower() in ['f', 'n', '0', 'false']:
        return False
    return default
