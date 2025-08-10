# 아래 함수를 수정하시오.
def reverse_string(string):
    result = ''
    for i in reversed(string):
        result += i
    return result



result = reverse_string("Hello, World!")
print(result)  
