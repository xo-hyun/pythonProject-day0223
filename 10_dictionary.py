# list    tuple       set     dictionary
# []       ()           {}      {}

# a,b  = 5,7
# print(a)
# print(b)

# data = 5,7              #packing
# print(data)
# a,b = data              #unpacking
# print(a)
# print(b)

a = {"홍길동", 20, "서울시 마포구 서교동"}
b = {
    "name":"홍길동",
    "age":20,
    "addr":"서울시 마포구 서교동"
}
print(b.items())
print(b.keys())
print(b.values())




# for row in b.items():
#     key,value = row     #unpacking
#     print(key,value)



# print(a, type(a))
# print(b, type(b))
#
# print(b['name'])
# print(b['age'])
# print(b['addr'])

