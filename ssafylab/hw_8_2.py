# 아래 함수를 수정하시오.
def check_number(numver):

    if type(numver) == int:
        if numver > 0:
            return '양수입니다.'
        elif numver < 0:
            return '음수입니다.'
        elif numver == 0:
            return "0입니다."
    else:    
        return '잘못된 입력입니다.'

print('숫자를 입력하세요 : ',end = '')
i = input()
try:
    i = int(i)
except ValueError:
    i = str(i)
print(check_number(i))
