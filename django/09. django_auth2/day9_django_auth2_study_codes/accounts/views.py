from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout  # as 별명을 지어주는 거고, 자유롭게

from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:  # 이미 로그인한 경우는 로그인하지 못하도록 설정
        return redirect('articles:index')
    
    # 실제로 로그인 과정이 처리되는 경우
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:  # GET method => 로그인 페이지를 반환
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    # request 정보 안에 쿠키가 들어있고, 쿠키 안에 세션 정보가 들어있어요.
    auth_logout(request)
    return redirect('articles:index')

from .forms import CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    # 회원가입을 진행하는 로직
    if request.method == "POST":
        # 회원가입 자체는 세션 데이터가 필요없다..
        # 실제로 사용자가 입력한 정보만 있으면 회원가입을 진행할 수 있음
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:  # method => GET, 회원가입 페이지를 반환하는 부분 
        form = CustomUserCreationForm()
    context ={
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 현재 로그인 된 유저 정보를 반환하는 친구 
    request.user.delete()
    return redirect('articles:index')