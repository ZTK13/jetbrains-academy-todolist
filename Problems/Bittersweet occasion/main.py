# finish the function
def find_the_parent(child):
    if issubclass(child, Drinks):
        print(Drinks.__name__)
    elif issubclass(child, Pastry):
        print(Pastry.__name__)
    elif issubclass(child, Sweets):
        print(Sweets.__name__)
    else:
        pass
