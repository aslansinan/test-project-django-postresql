from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ihalar', views.ihalar, name='ihalar'),
    path('ihalarim', views.ihalarim, name='ihalarim'),
]