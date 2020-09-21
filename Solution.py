def solve():
    if hidden_operation(False) is None:
        print("or")
        print(hidden_operation(False))

    elif hidden_operation(None) is None:
        print("and")
        print(hidden_operation(True))

    elif not hidden_operation(True):
        print("not")

    else:
        print("or")
        print(hidden_operation(False))
