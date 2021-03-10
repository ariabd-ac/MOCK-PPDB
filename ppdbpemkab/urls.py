from django.urls import path
from .import views


urlpatterns=[
  path('register/', views.Register, name='register'),
  path('login/', views.Login, name='login'),
  path('fun/', views.FunLogin, name='fun'),
  path('jalur-pendaftaran/', views.JalurPendaftaran, name='jalurPendaftaran'),
  path('jalur-pendaftaran/zonasi', views.Zonasi, name='Zonasi'),
  path('', views.Index, name='index'),
  path('form/', views.Form, name='form'),
]