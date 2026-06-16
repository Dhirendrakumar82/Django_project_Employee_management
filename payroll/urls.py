from django.urls import path
from . import views

urlpatterns = [

  path('payroll/', views.payroll_list, name='payroll_list'),

    path('payroll/add/', views.payroll_add, name='payroll_add'),
]