from django.contrib import admin
from django.urls import path,include
from  .views import *

urlpatterns = [
    path('home/',emp_home),
    path('add-emp/',add_emp),
    path('delete-emp/<int:emp_id>',delete_emp),
    path('update-emp/<int:emp_id>',update_emp),
    path('do-update-emp/<int:emp_id>',do_update_emp),
    path('add-department/',add_department),
    path('delete-department/<int:department_id>',delete_department),
    path('update-department/<int:department_id>',update_department),
    path('do-update-department/<int:department_id>',do_update_department),
    path('add-salary/',add_salary),
    path('delete-salary/<int:salary_id>',delete_salary),
    path('update-salary/<int:salary_id>',update_salary),
    path('do-update-salary/<int:salary_id>',do_update_salary),
    path('leave-request/',leave_request),
    path('delete-leave-request/<int:leave_id>',delete_leave_request),
    path('testimonials/',testimonials),
    
    
    ]