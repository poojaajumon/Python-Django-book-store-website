from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.lists, name='lists'),
    path('generic/', views.generic, name='generic'),
    path('add/', views.add, name='add'),
    path('lists/delete/<int:id>/', views.delete, name='delete'),
    path('lists/edit/<int:id>/', views.edit, name='edit'),
    path('objs/<int:id>/', views.detailed, name="detailed"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)