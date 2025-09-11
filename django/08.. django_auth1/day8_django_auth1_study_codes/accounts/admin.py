from django.contrib import admin
# 장고에서 제공하는 관리자 페이지 유저모델
from django.contrib.auth.admin import UserAdmin  
from .models import User  # 내가 만든 유저모델

# Register your models here.
admin.site.register(User, UserAdmin)