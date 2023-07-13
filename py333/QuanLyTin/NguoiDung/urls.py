from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('DSBaiViet/', views.DSBaiViet, name = 'DSBaiViet'),
    path('DangKy/', views.register, name="register"),
    #path('DangNhap/', views.login, name='hehe')#auth_views.LoginView.as_view(template_name="Page/DangNhap.html"), name="login"),
    #path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('login/',auth_views.LoginView.as_view(template_name="Page/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),


]
