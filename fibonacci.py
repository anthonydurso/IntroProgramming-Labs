def value(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return value(x-1) + value(x-2)
