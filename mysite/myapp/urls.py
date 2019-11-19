from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('add/', views.addRecipe),
    path('review/', views.reviewRecipe),
    path('view/<int:instance_id>/', views.viewRecipe),
    path('', views.home),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
    path('ingredient/<int:instance_id>/', views.addIng),
]
