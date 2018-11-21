from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/', views.SnippetList.as_view()),
    path('users/', views.UserList.as_view()),
    path('^users/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
