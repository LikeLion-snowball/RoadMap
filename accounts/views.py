from .models import CustomUser
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'form': form, 'error': '닉네임이나 비밀번호가 일치하지 않습니다.'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        elif request.POST['password1'] != request.POST['password2']:
            return render(request, 'signup.html', {'form': form, 'error': '비밀번호가 일치하지 않습니다.'})
        else:
            try:
                user = CustomUser.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'form': form, 'error': '이미 존재하는 닉네임입니다.'})
            except CustomUser.DoesNotExist:
                return render(request, 'signup.html', {'form': form, 'error': '올바른 비밀번호를 입력해주세요.'})
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})