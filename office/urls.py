# app/urls.py
from django.urls import path, reverse_lazy
from . import views

app_name = 'office'
urlpatterns = [
    path('company/', views.CompanyListView.as_view(), name='company_list'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('company/update/<uuid:pk>/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/delete/<uuid:pk>/', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('company/detail/<uuid:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),

]
