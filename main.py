# Теорія

# args
def black_hole(*args):  # args - arguments
    print(type(args))
    print(args)
    for arguments in args:
        print(args)


black_hole(2+2, "All")

# kwargs
def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key) # вивід окремо key або value словника

black_hole_named(name="Nick", planet='Earth', galaxy='Milky Way', age=1212121212*1.2)

