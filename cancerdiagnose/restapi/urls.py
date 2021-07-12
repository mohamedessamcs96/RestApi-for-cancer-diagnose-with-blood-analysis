from django.urls import path

from .views import userList
urlpatterns = [
    
    path('users/',userList.as_view()),
]