from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Sistemdeki tüm kullanıcıları listeleyen view
def users_page(request):
    users = User.objects.all()  # Tüm kullanıcıları alıyoruz.
    return render(request, 'auth/users.html', {'users': users})

# Profil sayfası
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'auth/profile.html', {'user': user})

# Şifre değiştirme işlemi
@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user
        if not user.check_password(old_password):
            messages.error(request, "Eski şifre yanlış.")
            return redirect("change_password")

        if new_password != confirm_password:
            messages.error(request, "Yeni şifreler uyuşmuyor.")
            return redirect("change_password")

        if len(new_password) < 6:
            messages.error(request, "Şifre en az 6 karakter olmalı.")
            return redirect("change_password")

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Kullanıcının oturumunu açık tutar
        messages.success(request, "Şifreniz başarıyla değiştirildi.")
        return redirect("dashboard")  # İstersen başka sayfaya yönlendir

    return render(request, "profile/change_password.html")