from django.shortcuts import render

from home.models import İhalarModel


def index(request):
    context = dict()
    ihalar =İhalarModel.objects.all()
    context["ihalar"] = ihalar
    return render(request, 'index.html', context)