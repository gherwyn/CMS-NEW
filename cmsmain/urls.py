from django.urls import path
from django.conf import settings
from . import views 
from django.conf.urls.static import static

app_name = 'cmsmain'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('processadd', views.processadd, name='processadd'),
    path('<int:projects_id>/detail/', views.detail, name='detail'),
    path('<int:projects_id>/delete/', views.delete, name='delete'),
    path('<int:projects_id>/edit/', views.edit, name='edit'),
    path('<int:projects_id>/processedit/', views.processedit, name='processedit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)