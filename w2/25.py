'''
absent = [2,5]
no_book = [7,8]
for student in range(1, 21):
    if student in absent:
        continue
    
    elif student in no_book:
        print("{0}번 저는 책이 없습니다".format(student))
    print("{0}번 학생 읽어보세요".format(student))'''

# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# students = ["iron man","thor","I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["iron man","thor","I am groot"]
# students = [i.upper() for i in students]
# print(students)

import random

# lit = [random.randint(5, 50) for _ in range(50)]
# for i in range(1, 51):
#     print("[{0}] )

cnt = 0
for i in range(1,51):
    time = random.randint(1,50)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))


