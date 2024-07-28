
def soma (x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=} A soma dos valores é:', x + y + z)
    else:
        print(f'{x=} {y=} A soma dos valores é:', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)

