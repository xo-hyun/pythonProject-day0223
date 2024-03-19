# 반복문 : while, for
# "hello"를 화면에 3번 출력
# n = 1
# while n <= 3:
#     print("hello")
#     n = n + 1
# print("완료")
# print(n)

# 연습) 사용자한테 n을 입력받아 1~n까지의 합을 누적하여 출력 해 봅니다.
# n = int(input("n을 입력=>"))
# i = 1
# sum = 0
# while i<=n:
#     sum += i
#     i+=1
# print("1에서 ",n,"까지의 합은 ",sum)

# 1에서 10까지의 모든 수를 출력
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i+=1

# 연습) 사용자 한테 n을 입력받아 n!을 구하여 출력하는 프로그램을 작성합니다.
# N?5
# 5*4*3*2*1=___
# n = int(input("n을 입력=>"))
# i = n
# r = 1
# while i >= 1:
#     r *= i
#     print(i,end=' ')
#     if i != 1:
#         print("*",end=' ')
#     i -= 1
# print("=",r)

'''
for 변수명 in range(시작,종료,증감):
    명령어

for 변수명 in range(시작,종료):       증감 1
    명령어
    
for 변수명 in range(종료):           시작 0, 증감 1
    명령

==> 종료-1 까지 동작
'''

# 1에서 10까지의 모든 수를 출력
# for i in range(1,11,1):
#     print(i, end=' ')

# for i in range(1,11):
#     print(i, end= ' ')
#
# for i in range(10):
#     print(i, end= ' ')

# 연습) 구구단 중에 2단을 출력 해 봅니다.
# dan = 2
# for i in range(1,10):
#     print(dan,"*",i,"=",dan*i)

# 연습) 2단부터 9단까지 모두 출력 해 봅니다.
for dan in range(2,10):
    print("***",dan,"단 ***")
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)
    print()


