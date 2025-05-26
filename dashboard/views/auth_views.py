import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, logout
from ..forms.auth_forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

# Hata loglarını kaydetmek için logger
logger = logging.getLogger('django')  # django logger'ı kullanıyoruz

def register(request):
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Kayıt başarılı! Giriş yapabilirsiniz.')
                return redirect('login')
            else:
                messages.error(request, 'Bir şeyler yanlış gitti. Lütfen tekrar deneyin.')
        else:
            form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})
    except Exception as e:
        # Hata loglarını kaydediyoruz
        logger.error(f"Beklenmeyen bir hata oluştu: {str(e)}")
        messages.error(request, f"Beklenmeyen bir hata oluştu: {str(e)}")
        return redirect('register')


def login_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Kullanıcı adı veya şifre yanlış.')
                # Hata logunu kaydediyoruz
                logger.warning(f"Başarısız giriş denemesi - Kullanıcı adı: {username}")
                return redirect('login')
        return render(request, 'auth/login.html')
    except Exception as e:
        # Hata loglarını kaydediyoruz
        logger.error(f"Giriş sırasında bir hata oluştu: {str(e)}")
        messages.error(request, f"Giriş sırasında bir hata oluştu: {str(e)}")
        return redirect('login')


def logout_view(request):
    try:
        logout(request)
        return redirect('login')
    except Exception as e:
        # Hata loglarını kaydediyoruz
        logger.error(f"Oturum kapatma sırasında hata oluştu: {str(e)}")
        messages.error(request, f"Oturum kapatma sırasında hata oluştu: {str(e)}")
        return redirect('dashboard')

def users_page(request):
    users = User.objects.all()
    return render(request, 'auth/users.html', {'users': users})


def reports_view(request):
    return render(request, 'auth/reports.html')

def settings_view(request):
    return render(request, 'auth/settings.html')