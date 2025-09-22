list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'f']

zipfile = list(zip(list1, list2))
print(zipfile)

zipfile = tuple(zip(list1, list2))
print(zipfile)

zipfile = dict(zip(list1, list2))
print(zipfile)

zipfile = set(zip(list1, list2))
print(zipfile)

n , v  =  zip(*zipfile)
print(n)
print(v)