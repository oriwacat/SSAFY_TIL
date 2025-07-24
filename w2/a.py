'''
# 집합 (set)
# 중복 안됨, 순서없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"김씨", "빅씨", "최씨"}
python = set(["김씨", "최씨"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 수 없는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김대호")
print(python)

# java 를 잊음
java.remove("최씨")
print(java) '''

'''# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))'''

"""
from random import *
lit = [1,2,3,4,5]
print(lit)
shuffle(lit)
print(lit)
print(sample(lit, 1)) """

from random import *
lit = range(1, 21)
lit = list(lit)
shuffle(lit)
'''
print("-- 당첨자 발표 --")
print("치킨 당첨자 :", lit.pop())
print("커피 당첨자 :", sample(lit, 3))
print("-- 축하합니다 --")'''

winners = sample(lit, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]) )
print("커피 당첨자 : {0}".format(winners[1:]) )
print("-- 축하합니다 --")
