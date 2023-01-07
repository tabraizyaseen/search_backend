from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticketSearchableFields.as_view()),
    path('<str:value_name>/', views.ticketSearchValue.as_view()),
]