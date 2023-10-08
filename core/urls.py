
from django.contrib import admin
from django.urls import path,include

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.DashboardView.as_view(),name='index'),
    path('api/', include('api.urls')),
]
