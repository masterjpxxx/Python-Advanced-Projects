def alternate_even_odd():
    count = 0
    while True:
        if count %2 == 0:
            yield 'Even!'
        else:
            yield 'Odd!'
        count += 1
    
generator = alternate_even_odd()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))