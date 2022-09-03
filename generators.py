def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

#yield is kind of like return. function will stop here until the generator
#is called again. 

for num in gen_range(10, step=2):
    print(num)

#This is a fibonacci generator
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
        