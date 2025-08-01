def restructure_word(word, arr):
    for i in word:
        if i.isdecimal():
            for _ in range(int(i)):
                if arr:         # arr이 비어있지 않은 경우만 pop
                    arr.pop()
        else:
            if i in arr:       # 존재할 때만 제거
                arr.remove(i)
    return arr


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)
print(arr)
result = restructure_word(word, arr)
print(result)

print(''.join(result))
