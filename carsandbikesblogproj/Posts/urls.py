from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from .views import LogoutView, custom_logout, register, add_post, edit_post
from .views import posts_list, post_details_view, user_login

urlpatterns = [
    path('', posts_list, name='home_path'),
    path('post/<int:passed_id>/', post_details_view,name='detail_path'),
    # path('login/',user_login, name='login')
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', custom_logout, name='logout'),
    path('account/register/', register, name='register'),
    path('account/add_post/', add_post, name='add_post'),
    path('account/edit_post/<int:passed_id>/', edit_post, name='edit_post'),
    path('account/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('account/password-change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
