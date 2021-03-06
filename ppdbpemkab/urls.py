from django.urls import path
from .import views


urlpatterns=[
  

  path('', views.Index, name='index'),
  path('form/', views.Form, name='form'),
  path('pendaftar/', views.Pendaftar, name='pendaftar'),
  path('operator/', views.Operator, name='operator'),
  path('operatorlogin/', views.OperatorLogin, name='operatorlogin'),
  path('operator/logout', views.Logout, name='operatorlogout'),
  path('siswa/dashboard', views.DashboardSiswa, name='dashboardsiswa'),
  # siswa
  path('register/', views.Register, name='register'),
  path('login/', views.Login, name='login'),
  path('loginsiswa/', views.LoginSiswa, name='loginsiswa'),
  path('jalur-pendaftaran/', views.JalurPendaftaran, name='jalurPendaftaran'),
  path('jalur-pendaftaran/zonasi', views.Zonasi, name='zonasi'),
  path('siswa/dashboard', views.DashboardSiswa, name='dashboardsiswa'),
  path('siswa/logout', views.SiswaLogout, name='siswalogout'),
]