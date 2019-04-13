def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please Provide a string Argument')
    return x.capitalize()
