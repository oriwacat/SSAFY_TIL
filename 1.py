import pprint

n =10
list1 = [[i]*n for i in range(n)]


pprint.pprint(list1)
print('-'*100)

#전치행렬
list2 = list(map(list, zip(*list1)))
print('전치행렬')
pprint.pprint(list2)
print('-'*100)

#90도 시계 방향 회전
list3 = list(zip(*list2[::-1]))
print('90도')
pprint.pprint(list3)
print('-'*100)

#90도 반시계 방향 회전
list4 = list(zip(*list3))[::-1]
print('-90도')
pprint.pprint(list4)
print('-'*100)


