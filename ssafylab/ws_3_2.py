number_of_people = 0


def increase_user():
    global number_of_people
    print('현재 가입 된 유저 수 :', number_of_people)
    number_of_people += 1
    


def create_user(name, age, address):
    increase_user()
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(name,'님 환영합니다!')
    return user_info
 
user = create_user('홍길동', 30, '서울')
print(user)
print('현재 가입 된 유저 수 :', number_of_people)
