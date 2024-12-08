# 7. Using a Generator
def add_gen(x, y):
    yield x + y

gen = add_gen(24, 8)
print(next(gen))
