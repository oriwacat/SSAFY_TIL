from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout  
from django.contrib.auth.decorators import login_required

def login(request):   
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


def logout(request):
    pass


def signup(request):
    pass


def delete(request):
    pass