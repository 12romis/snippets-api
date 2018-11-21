from django.urls import path
from app import views

urlpatterns = [
    path('<int:pk>/', views.snippet_detail),
    path('', views.snippet_list),
]
