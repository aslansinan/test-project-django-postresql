import base64
import json
from http import HTTPStatus
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from account import forms
from account.forms import UyeKayitFormu
from account.models import Uye


def indexaccount(request):
    return render(request, 'account/index.html')


def login_request(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)  # POST verileri ile formu oluşturun

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            # authenticate fonksiyonunu kullanarak kimlik doğrulama yapın
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Giriş başarılı")
                return redirect('index')

        # Form geçerli değilse veya kimlik doğrulama başarısız olduysa hata mesajı verin
        messages.error(request, "Giriş sırasında hata oluştu. Lütfen tekrar deneyin.")

    return render(request, 'login.html', {'form': forms.LoginForm()})

def yeni_uye_kayit(request):
    if request.method == "POST":
        form = UyeKayitFormu(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Kayıt başarılı")
            return redirect('index')  # 'index' yerine kendi sayfa adınıza göre güncelleyin
        else:
            messages.error(request, "Kayıt sırasında hata oluştu. Lütfen tekrar deneyin.")
            return redirect('index')  # 'index' yerine kendi sayfa adınıza göre güncelleyin
    return render(request, 'signup.html')

def logout_request(request):
    logout(request)
    return redirect("index")


def anonymous_required(function=None, redirect_url = None):
    if not redirect_url:
        redirect_url = 'index'
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url= redirect_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@anonymous_required
def forget_password(request):
    if request.method == "POST":
        uye_email = request.POST.get("email")
        if uye_email:
            try:
                uye = Uye.objects.get(email=uye_email)
            except Uye.DoesNotExist:
                messages.error(request, "Bu email'e sahip kullanıcı bulunamadı...")
                return redirect("forget-password")
        else:
            return redirect("forget-password")

        mail_dict = dict()
        encoded = base64.b64encode(str(uye_email).encode('ascii'))
        formatlama = str(encoded).replace("'", "/")[1:]
        # url = "http://127.0.0.1:8000/account/mail/change-password" + formatlama
        url = "https://http://127.0.0.1:8000/account/mail/change-password" + formatlama
        mail_dict["hashed_url"] = url
        html_content = render_to_string('email-icerikleri/sifre-degistirme-mail.html', mail_dict)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Şifre Sıfırlama.",
            text_content,
            'noreply@penfest.com.tr',
            [uye.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        messages.success(request, "Şifre Sıfırlama Mailiniz Gönderildi...")
        return redirect("index")
    else:
        return render(request, "sifremi_unuttum.html")