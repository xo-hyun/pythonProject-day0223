# list    tuple       set     dictionary
# []       ()           {}      {}

# set   : 중복을 허용하지 않는 자료구조

a = [1,3,5,7,5,7,9]
b = {1,3,5,7,5,7,9}
print(a,type(a))
print(b,type(b))

a = set(a)
print(a, type(a))
