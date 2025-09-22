# my_set = {1,2,3,4,5,6,7,8,9}
# print(my_set)

# set = {1,2,3,4,4}
#-------------- operation in set-----------------
# set.add("mango")
# print(set)
# set.update([ "orange"])
# print(set)
# set.remove("orange")
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
#------------- Membership test---------------
# my_set = {1,2,3,4,5,6,7,8,9}
# print(1 in my_set)
# print(10 in my_set)
# print(10 not in my_set)

# -------------Mathematical operation-----------------
# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A|B)
# print(A&B)
# print(A-B)
# print(B-A)
# print(A^B)

# ---------Set Methods ------------
# A = {1, 2, 3}
# B = {1, 2}
# C = {1, 2, 3, 4, 5}

# print(B.issubset(A))
# print(A.issubset(B))
# print(A.issuperset(B))
# print(A.isdisjoint(C))
# print(C.isdisjoint(A))

# --------- Forsen Set (Immutable Set)-----------------

# A  = frozenset([1,2,3])
# # A.add(4)
# print(A)

# ------------ Practical Example ----------------
# number = [1,2,3,4,4,5]
# unique = set(number)
# print(unique)

# students_A = {"Rahim", "Karim", "Sakib"}
# students_B = {"Sakib", "Jamil", "Rahim"}

# print(students_A & students_B)

s = {x**2 for x in range(1,6)}
print(s)