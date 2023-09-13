from django.contrib import admin
from django.urls import path, include

import account

urlpatterns = [
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
