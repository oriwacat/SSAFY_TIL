# 아래 함수를 수정하시오.
def capitalize_words(hihi):
    ss = ''
    a = hihi.split()
    for i in a:
       ss += i.capitalize() + ' '
    return ss.strip()


result = capitalize_words("hello, world!")
print(result)
