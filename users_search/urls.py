from django.urls import path
from . import views

urlpatterns = [
    path('', views.userSearchableFields.as_view()),
    path('<str:value_name>/', views.userSearchValue.as_view()),
]