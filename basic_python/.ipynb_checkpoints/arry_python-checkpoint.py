# a = [1,2,3,4,5,6]

# print(a)

# mixt  = [1 , "apple" , 3.1 , True]
# print(mixt)

#------------------ Accessing Eletemts-------------- 
# number = [10,20,30,40,50]

# print(number[0])
# print(number[-1])

# # Slicing 

# print(number[1:4])
# print(number[:3])
# print(number[::3])

# --------------- Modifying List -----------------------

# number = [10,20,30]

# number[1] = 25
# print(number)


# -----funciton in arr-----

# number.append(40)
# print(number)
# number.insert(1,16)
# print(number)
# number.extend([50 , 60])
# print(number)

# number.remove(25)
# print(number)
# number.pop(1)
# print(number)
# number.clear()
# print(number)


# ---------array Operation------------
# number = [1,2,3]
# number1 = [4,5,6]

# print(number + number1)
# print(number * 2)

# print(2 in number)
# print(7 in number)

# ----------🔹 5. Loop through List-------------
a = [10,20,30,40,50,60]
# for a in a :
#     print(a)

# for i , a in enumerate(a):
#     print(i , a)

# ----------🔹 6. List Comprehension (Advance)----------

# s = [x**2 for x in range(1,6)]
# print(s)

# even = [x for x in range(1,11) if x % 2 == 0]
# print(even)

# matrix = [[1,3,4],[4,5,6]]
# flat = [num for row in matrix for num in row]
# print(flat)


# -----------------🔹 7. Useful List Methods---------------
# number  = [3,1,4,2,5]
# print(len(number))
# print(max(number))
# print(min(number))
# print(sum(number))
# number.sort()
# print(number)
# number.reverse()
# print(number)

# ----------------🔹 8. Multi-Dimensional Lists-----------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print(col, end=" ")
    print() 
