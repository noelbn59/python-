def square_generator(n):
    for i in range(1,n+1):
        yield i* i
n=int(input("Enter a number:"))
g = square_generator(n)

print(next(g))
print(next(g))


# def square(n):
#     yield n*n
# n=int(input("Enter a number:"))
# g=square(n)
# print(next(g))
