def my_numbers():
    a = 1
    while True:
        yield a
        a += 2


mygen = my_numbers()

print(next(mygen))
input('press enter')
print(next(mygen))
print(next(mygen))
print(next(mygen))
