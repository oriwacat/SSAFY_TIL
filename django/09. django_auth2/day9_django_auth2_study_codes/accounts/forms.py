
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model

# 우리가 원하는건 연결하는 유저 모델만 바꾸고 싶다.
# 기존에 만들어져 있는 UserCreationForm 모델을 상속 
class CustomUserCreationForm(UserCreationForm):
    # 유저 연결하는 부분은 Meta 클래스에 선언되어 있다. 
    class Meta(UserCreationForm.Meta):
        # 유연하게 동작하기 위해서, 하드코딩 하지 않는다. 
        model = get_user_model()