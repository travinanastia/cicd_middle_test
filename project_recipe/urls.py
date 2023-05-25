from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('category_list/', views.category_list, name='category_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)