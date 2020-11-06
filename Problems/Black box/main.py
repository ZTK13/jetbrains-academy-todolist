# use the function blackbox(lst) that is already defined
lst = list(range(10))
if id(lst) == id(blackbox(lst)):
    print("modifies")
else:
    print("new")
