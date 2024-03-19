# 연습) 두개의 수를 매개변수로 전달받아 그 중에 큰 수를 찾아 반환하는 함수를
# 만들고 호출 해 봅니다
def max(a,b):
    if b > a: a = b
    return a

def max3(a,b,c):
    return max( max(a,b), c )
#연습) 3개의 수를 매개변수로 전달받아 그 중에 큰수를 찾아 반환하는 함수를
# 만들고 호출 해 봅니다.  두 수중에 큰수 찾는 함수를 활용합니다.
print(max3(10,5,9))
print(max3(9,10,7))
print(max3(9,10,70))








# print(max(2,3))
# print(max(10,5))
# print(max(2,2))
