# Теорія

# args
"""def black_hole():  # args - arguments
    print(type(args))
    print(args)
    for arguments in args:
        print(args)


black_hole(2+2, "All")"""

# kwargs
"""def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key) # вивід окремо key або value словника

black_hole_named(name="Nick", planet='Earth', galaxy='Milky Way', age=1212121212*1.2)
"""
def black_hole_full(*args, **kwargs):
    if not args:  # перевірка наявності неіменованих аргументів
        return 0
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(key, value)

black_hole_full(123, name="Nick", planet='Earth', galaxy='Milky Way', age=1212121212*1.1)

