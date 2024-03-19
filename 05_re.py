import re

db = '''
    3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1234  Tiger 567
1548  Kerry 534
'''
print(db)

'''
기호 앞에 문자에 대한 설정
?	1번이하 colou?r ==> "color"와 "colour"
*	0번이상 ab*c ==> "ac", "abc", "abbc", "abbbc" 
+	1번이상 ab+c ==> "abc", "abbc", "abbbc"
'''
# 숫자만 출력 해 봅니다.
# result = re.findall("[0-9]+",db)
# print(result)
# print(type(result))

# 연습)이름만 출력해 봅니다.
# names = re.findall("[A-z]+",db)
# names = re.findall("[A-Z][a-z]+",db)
# print(names)

# 연습)전화번호만 출력 해 봅니다.
# phones = re.findall("[0-9][0-9][0-9][0-9]",db)
# phones = re.findall("[0-9]{4}",db)
# phones = re.findall("\d{4}",db)
# phones = re.findall("^\d+",db, re.MULTILINE)
# re.MULTILINE : 찾고자 하는 데이터가 줄 마다 있어요!
# print(phones)

# 연습) 아이디만 추출하여 출력 해 봅니다.
# ids = re.findall("\d{3}",db)
# ids = re.findall("\d+$", db, re.MULTILINE)
# print(ids)

# 연습) T로 시작하는 이름만 찾아서 출력 해 봅니다.
startT = re.findall("T[a-z]+", db)
print(startT)

# 연습) T로 시작하지 않은 이름만 출력 해 봅니다.
# notT = re.findall("[^T][a-z]+",db)
# print(notT)
# ['Bob', 'Jonny', 'Kate', 'ony', 'Peter', 'Alice', 'iger', 'Kerry']

# notT = re.findall('[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+',db)
notT = re.findall('[A-SU-Z][a-z]+',db)
print(notT)



