from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인, 인증이 성공한거다.. 
            # 서버는 세션 데이터를 만들고, DB에 저장해야 한다.
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:  # method => GET
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
