from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from EmployeeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("department", include('EmployeeApp.urls')),
    path("employee", views.employeeApi),
]
