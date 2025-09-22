mun = [1,2,3,4,5,6,7]

# def sq(x):
#     return x**x
# print(sq(3))


# syntex map(funciton , iteable object)
# num = map(lambda x :x**2, mun)
# print(list(num))

# num = filter(lambda mun:mun%2==1 , mun )

# print(list(num))

from functools import reduce
s = reduce(lambda a  , b:a+b , mun)

print(s)

print(sum(mun))