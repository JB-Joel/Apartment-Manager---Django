from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='apt-home'), #main home-page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:pk>', views.apartDetails, name='apart_details'),
    path('new-apt/', views.createApt, name='add'),
    path('new-tenant-<str:pk>/', views.createTenant, name='add-tenant'),
]