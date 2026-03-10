x=3
match x:
    case 0:
        print("x is 0")
    case 2:
        print("x is 2")
    case _ if(x!=3):
        print("x is not 3")
    case _:
        print("x is something else")