# list    tuple      set      dictionay
# []        ()        {}      {}

# 튜플: 리스트의 상수버전
a = [1,3,5,7]
b = (1,3,5,7)
b = list(b)
print(type(b))
b.append(9)
b[0] = 100
b = tuple(b)
print(type(b))
print(b)

# print(a,type(a))
# print(b,type(b))
# # b.append(10);
# # print(b)
# print(b[0])
# # b[0] = 100
# for i in b:
#     print(i, end=" ")

