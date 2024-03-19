import re
import requests

url = "https://devweather.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

text = requests.get(url).text
# print(text)
# title = re.findall('<title>(.+)</title>', text)
# print(title)
# for row in title:
#     print(row)

# re.DOTALL    ==> 찾고자 하는 시작, 마지막 패턴이 여러줄에 걸쳐 있어요.
# .+    ==> 탐욕적
# .+?   ==> 비탐욕적

# list = re.findall('<location wl_ver="3">(.+)</location>', text, re.DOTALL)
# print(len(list))
# 1

list = re.findall('<location wl_ver="3">(.+?)</location>', text, re.DOTALL)
print(len(list), type(list))
# 41
'''
<tmEf>2024-02-26 00:00</tmEf>
<wf>맑음</wf>
<tmn>-1</tmn>
<tmx>7</tmx>
'''
# 연습) 모든 도시명을 추출하여 출력 해 봅니다.,
for row in list:
    city = re.findall("<city>(.+)</city>", row)
    data = re.findall('<data>(.+?)</data>', row,re.DOTALL)
    for d in data:
        tmEf = re.findall('<tmEf>(.+?)</tmEf>',d)
        wf  = re.findall('<wf>(.+?)</wf>',d)
        tmn = re.findall('<tmn>(.+?)</tmn>',d)
        tmx = re.findall('<tmx>(.+?)</tmx>',d)
        print(city[0], tmEf[0], wf[0], tmn[0], tmx[0])