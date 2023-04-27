
people = [("Alex", 16), ("Oleksandr", 18), ("Bob", 23)]

def dicts(*args, **kwargs):
    name_age = {}
    if args: # поки не закінчаться елементи списку
        for tup in args[0]:
            name, age = tup
            name_age[name] = age
    return name_age
print(dicts(people))

