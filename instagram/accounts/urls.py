from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser),
    path('login/', views.loginUser, name='login'),
    path('profile/', views.profile, name="profile"),
    path('follow/<int:id>',views.follow,name="follow")
]