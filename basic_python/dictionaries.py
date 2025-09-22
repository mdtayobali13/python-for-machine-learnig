# # ---------2️⃣ Basic Operations-----------------

# dic = {
#     'name' : 'Md.Tayob ali',
#     "varsity" : "DIU",
#     "Roll" : 12
# }

# dic["semeter"] = 4
# dic['age'] = 20
# dic['Dept'] = "CSE"

# print(dic)
# print(dic['name'])
# print(dic["varsity"])
# print(dic["semeter"]) 
# print(dic["age"]) 
# print(dic["Dept"]) 

# del dic['Dept']
# print(dic)
# dic.pop('semeter')
# print(dic)
# # dic.clear()
# # print(dic)

# print('name'  in dic)


# ---------------3️⃣ Looping through Dictionary-------------

# dic = {
#     'name' : 'Md.Tayob ali',
#     "varsity" : "DIU",
#     "Roll" : 12
# }

# for kye in dic :
#     print(kye)

# for val in dic.values():
#     print(val)

# for key , val in dic.items():
#     print(key ,":", val)

# dic.update({'city' : 'Dinajpur' , 'age' : 20})
# print(dic)
# dic.pop("age")
# print(dic)
# dic.popitem()
# print(dic)
# dic.clear()
# print(dic)

# --------------------5️⃣ Nested Dictionary----------------
# students = {
#     "s1": {"name": "Rahim", "age": 21},
#     "s2": {"name": "Karim", "age": 22}
# }

# print(students["s1"]["name"])
# print(students["s2"]["name"])

# -------------6️⃣ Dictionary Comprehension (Intermediate)---------------
# s = {x:x**2 for x in range(1,6)}
# print(s)


# -------------6️⃣ Dictionary Comprehension (Intermediate)---------------

# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}

# c = a|b
# print(c)

# a.update(b)
# print(a)