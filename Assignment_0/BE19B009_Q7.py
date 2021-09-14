def sqaure_generator():
    for i in range(100):
        print("Your next number is")
        yield(i**2)
gen = sqaure_generator()
for i in range(3): print(next(gen))
