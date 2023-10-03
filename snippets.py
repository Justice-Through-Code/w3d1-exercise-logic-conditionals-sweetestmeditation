
'''
Debug the following code snippets so that they all run successfully
'''


def snippet_1():
    u = 5
    v = 2

    if u * v == 10:  # Fixed the comparison operator from '=' to '=='
            print(f"The product of u ({u}) and v ({v}) is 10")
    else:
            print(f"The product of u ({u}) and v ({v}) is not 10")


def snippet_2():
    x = 15
    y = 25
    z = 30

    if z < x:
        print("z is less than x")

    elif z > x and z < y:  # Added ':' after the condition
        print("z is between x and y")

    else:  
        print("z is greater than y")


def snippet_3():
    # TODO: Modify the comparison operator below so the `assert` statement passes
    # TODO: Update the print statement to reflect the fact that a 'is equal to' b

    a = 1
    b = 1
    c = (a == b)   # Modified the comparison operator to '=='

    print(f"The value of c ({c}) is True since a ({a}) is equal to b ({b}).")
    assert(c == True)  # <-- DO NOT EDIT THIS LINE


def snippet_4():
    # TODO: Modify exactly one boolean operator in the assignment of d, so that d evaluates to False

    d = (5 < 7) and not (8 < 20)  # Changed the boolean operator 'or' to 'and'

    # TODO: Explain how d is set to False in a comment
    assert(d == False)  # <-- DO NOT EDIT THIS LINE

    # The value of `d` was initially set to `True` because of the `or` operator.
    # However, by changing it to `and`, both conditions now need to be True for `d` to be `True`. 
    # The second condition is `False`, so `d` is set to `False`.


def snippet_5():
    # TODO: Modify the comparison operator so o evalutes to true
    # TODO: Update the print statement to reflect the changes

    m = "GOAT"
    n = "goat"

    o = (m != n)  # Modified the comparison operator and used '!='

    print (f"The value of o ({o}) is True since Python is case-sensitive.")
    assert(o == True)  # <-- DO NOT EDIT THIS LINE

snippet_1()
snippet_2()
snippet_3()
snippet_4()
snippet_5()