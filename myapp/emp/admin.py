from django.contrib import admin
from .models import *

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','emp_id','phone','department','address','working')
    search_fields=('name',)
    list_filter=('working',)
admin.site.register(Emp,EmpAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name','department_id','phone','working')
    search_fields=('name',)
admin.site.register(Department,DepartmentAdmin)


class SalaryAdmin(admin.ModelAdmin):
    list_display=('name','salary_id','account_no','date','amount')
    search_fields=('account_no',)
admin.site.register(Salary,SalaryAdmin)

class LeaveAdmin(admin.ModelAdmin):
    list_display=('name','leave_id','subject','start_date','end_date','apruval')
    search_fields=('name',)
admin.site.register(Leave,LeaveAdmin)

admin.site.register(Testimonial)



