# 함수 : 어떤 문제해결을 위한 서로 관련있는 명령어 들의 집합
'''
def 함수이름():
    명령어들
    return [값1, 값2, ..]

파이썬의 함수를 여러개의 값을 반환할 수 있어요!
이것을 packing해서 tuple로 받을 수도 있고
unpacking하여 따로따로 받을 수도 있어요.
'''

# 두개의 수를 매개변수로 전달받아 더하기 하여 결과를 돌려주는 함수
# def add(a,b):
#     r = a + b
#     return r
#
# r = add(5,2)
# print(r)
# print(add(5,2))
# print(add(8,15))




# 두개의 수를 매개변수로 전달받아
# 더하기, 빼기, 곱하기, 나누기 한 결과를 반환하는 함수를 만들어 봅시다.
def calc(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a//b
    return add,sub,multi,div

data = calc(5,2)
print(data)
add, sub, multi, div = data
print(add,sub,multi,div)

# add,sub,multi,div = calc(5,2)
# print(add,sub,multi,div)




