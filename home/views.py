from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Uye
from home.forms import IhaUyeForm
from home.models import İhalarModel, İhaUyeModel


def index(request):
    return render(request, 'index.html')

def ihalar(request):
    context = dict()
    ihalar = İhalarModel.objects.all()
    if request.method == "POST":
        ihaid = request.POST.get("ihaid")
        try:
            iha = İhalarModel.objects.get(id=ihaid)
            uye = request.user
            sinav, _ = İhaUyeModel.objects.update_or_create(
                ihalar=iha,
                uye=uye,
            )
            sinav.save()
            messages.success(request, "Ekleme başarılı")
            return redirect('ihalarim')  # Kiralama işlemi tamamlandıktan sonra yönlendirilecek sayfa
        except İhalarModel.DoesNotExist:
            # İha bulunamadı
            pass
    context["ihalar"] = ihalar
    return render(request, 'ihalar.html', context)


def ihalarim(request):
    context = dict()
    ihalarim = İhaUyeModel.objects.all()
    ihalarim_list = list(ihalarim)  # QuerySet'i bir liste haline getirin
    context["ihalarim"] = ihalarim_list
    return render(request, 'ihalarim.html',context)

def guncelle_ihala(request, ihala_id):
    iha = get_object_or_404(İhaUyeModel, pk=ihala_id)
    uyeler= Uye.objects.all()
    ihalar = İhalarModel.objects.all()
    if request.method == "POST":
        form = IhaUyeForm(request.POST, instance=iha)  # İlgili formu oluşturun ve mevcut veri ile doldurun
        if form.is_valid():
            form.save()  # Formu kaydedin
            messages.success(request, "Ekleme başarılı")
            return redirect('ihalar')  # Başarılı güncelleme sonrası yönlendirme

    else:
        form = IhaUyeForm(instance=iha)  # GET isteği için boş form oluşturun

    return render(request, 'guncelle_ihala.html', {'iha': iha,'uyeler': uyeler,'ihalar': ihalar, 'form': form})

def sil_ihala(request, ihala_id):
    iha = get_object_or_404(İhaUyeModel, pk=ihala_id)
    # İha'yı silmek için gerekli işlemleri yapın
    messages.success(request, "Silme başarılı")
    iha.delete()
    # Silme işlemi tamamlandıktan sonra yönlendirme yapın
    return redirect('ihalar')  # Sil