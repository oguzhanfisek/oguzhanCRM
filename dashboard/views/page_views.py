from django.shortcuts import render

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        # Buraya form işlemleri eklenebilir, e-posta gönderme vs.
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Gelen mesaj: {name} - {email} - {message}")
        # Not: Production'da bu log'u sil ve düzgün e-posta sistemi kur.
    return render(request, 'pages/contact.html')
