# 아래 함수를 수정하시오.
def remove_duplicates(hihi):    
    new_lst = list(set(hihi))
    
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 3, 3, 5, 5, 1, 4, 4, 5])
print(result)
