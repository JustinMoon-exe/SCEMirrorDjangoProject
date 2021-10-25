from . import views
from django.urls import path

urlpatterns = [
    path(r'donate/', views.donate_page, name='donate'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
    path(r'logout/', views.logout, name='logout'),
    path(r'admin_page/', views.admin_page, name='admin_page'),
    path(r'gallery/', views.gallery, name='gallery'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]