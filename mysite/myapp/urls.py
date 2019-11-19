from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('add/', views.addRecipe),
    path('view/<int:instance_id>/', views.viewRecipe),
    path('review/<int:instance_id>/', views.reviewRecipe),
    path('', views.home),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
]
