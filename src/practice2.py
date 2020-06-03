def add(a,b):
    if type(a) is int:
        if type(b) is int:
            return str(a)+str(b)
        else:
            return None
    if type(a) is str:
        if type(b) is str:
            return (a+b)

