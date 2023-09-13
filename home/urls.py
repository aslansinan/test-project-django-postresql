from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ihalar', views.ihalar, name='ihalar'),
    path('ihalarim', views.ihalarim, name='ihalarim'),
    path('ihala/<int:ihala_id>/guncelle/', views.guncelle_ihala, name='guncelle_ihala'),
    path('ihala/<int:ihala_id>/sil/', views.sil_ihala, name='sil_ihala'),
]