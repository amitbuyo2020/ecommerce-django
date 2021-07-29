from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout_user'),
    path('register/', views.register, name='register_user'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('profile/', views.profile, name='profile')

]