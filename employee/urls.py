from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path(
        'employees/',
        views.employee_list,
        name='employee_list'
    ),

    path(
        'employees/add/',
        views.employee_add,
        name='employee_add'
    ),

    path(
        'employees/edit/<int:pk>/',
        views.employee_edit,
        name='employee_edit'
    ),

    path(
        'employees/delete/<int:pk>/',
        views.employee_delete,
        name='employee_delete'
    ),
]



# from django.urls import path
# from . import views

# urlpatterns = [

#     path(
#         '',
#         views.employee_list,
#         name='employee_list'
#     ),

#     path(
#         'add/',
#         views.employee_add,
#         name='employee_add'
#     ),

#     path(
#         'edit/<int:pk>/',
#         views.employee_edit,
#         name='employee_edit'
#     ),

#     path(
#         'delete/<int:pk>/',
#         views.employee_delete,
#         name='employee_delete'
#     ),

# ]





# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),

#     path('employees/',
#          views.employee_list,
#          name='employee_list'),

#     path('employees/add/',
#          views.employee_add,
#          name='employee_add'),

#     path('employees/update/<int:pk>/',
#          views.employee_update,
#          name='employee_update'),

#     path('employees/delete/<int:pk>/',
#          views.employee_delete,
#          name='employee_delete'),
# ]