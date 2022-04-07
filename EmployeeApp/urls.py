from EmployeeApp import views
from django.urls import path
from django.conf.urls import include

urlpatterns =[
    path("",views.departmentApi),
    path("/<int:id>",views.departmentApi),

    path("employee",views.employeeApi),
    path("/<int:id>",views.employeeApi),
]

