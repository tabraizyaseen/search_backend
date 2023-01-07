from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizationSearchableFields.as_view()),
    path('<str:value_name>/', views.organizationSearchValue.as_view()),
]