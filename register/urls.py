from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list,name='employee-list'),
    path('create/',views.employee_create,name='employee-create'),
    path('update/<int:id>/',views.employee_update,name='employee-update'),
    path('delete/<int:id>',views.employee_delete,name='employee-delete'),
    
]

