# 파이썬에서의 자료구조
# list      tuple       set         dictionary
# []        ()          {}          {}

a = [1,3,5,7]
a.append(9)
print(a)
a[0] = 100
print(a)


# 연습) 리스트의 요소를 거꾸로 출력 해 봅니다.
# for i in range(len(a)-1, -1, -1):
#     print(a[i], end= " ")
# print()
# for i in reversed(a):
#     print(i, end= " ")

# print(a)
# print(type(a))
#
# print(a[0])
# print(a[1])
# print(a[4])
# IndexError: list index out of range
# print(len(a))
#
# for i in range(0,len(a)):
#     print(a[i], end= " ")
# print()
# for i in range(len(a)):
#     print(a[i], end= " ")
# print()
# for i in a:
#     print(i, end= " ")