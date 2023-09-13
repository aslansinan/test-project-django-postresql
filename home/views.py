from django.shortcuts import render

from home.models import İhalarModel


def index(request):
    return render(request, 'index.html')

def ihalar(request):
    context = dict()
    ihalar = İhalarModel.objects.all()
    context["ihalar"] = ihalar
    return render(request, 'ihalar.html',context)

def ihalarim(request):
    return render(request, 'ihalarim.html')