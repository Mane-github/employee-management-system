from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Department,Salary,Leave,Testimonial



# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()
    departments=Department.objects.all()
    salarys=Salary.objects.all()
    leaves=Leave.objects.all()
    
    return render(request,'emp/home.html',{
        'emps':emps,'departments':departments,'salarys':salarys,'leaves':leaves
    })

def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        emp_phone=request.POST.get('emp_phone')
        
        emp_address=request.POST.get('emp_address')
        emp_department=request.POST.get('emp_department')
        emp_working=request.POST.get('emp_working')
        
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
            
            e.save()
                
            
        
        
        
        
        return redirect('/emp/home/')
    
    return render(request,'emp/add_emp.html',{})



def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')


def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,'emp/update_emp.html',{
        'emp':emp
    })
    
def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get('emp_name')
        emp_id_temp=request.POST.get('emp_id')
        emp_phone=request.POST.get('emp_phone')
        
        emp_address=request.POST.get('emp_address')
        emp_department=request.POST.get('emp_department')
        emp_working=request.POST.get('emp_working')
        
        e=Emp.objects.get(pk=emp_id)
        
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
            
        e.save()    
    
    return redirect("/emp/home/")
    
def add_department(request):
    if request.method=="POST":
        
        department_name=request.POST.get('department_name')
        department_id=request.POST.get('department_id')
        department_phone=request.POST.get('department_phone')
        department_working=request.POST.get('department_working')
        
        d=Department()
        
        d.name=department_name
        d.department_id=department_id
        d.phone=department_phone
        if department_working is None:
            d.working=False
        else:
            d.working=True
            
            d.save()
            
            
            
        return redirect('/emp/home/')
    return render(request,'emp/add_department.html',{})


def delete_department(request,department_id):
    department=Department.objects.get(pk=department_id)
    department.delete()
    return redirect('/emp/home/')

def update_department(request,department_id):
    department=Department.objects.get(pk=department_id)
    
    return render(request,'emp/update_department.html',{
        'department':department
    })

def do_update_department(request,department_id):
    if request.method=="POST":
        department_name=request.POST.get('department_name')
        department_id_temp=request.POST.get('department_id')
        department_phone=request.POST.get('department_phone')
        department_working=request.POST.get('department_working')
        
        d=Department.objects.get(pk=department_id)
        
        d.name=department_name
        d.department_id=department_id_temp
        d.phone=department_phone
        if department_working is None:
            d.working=False
        else:
            d.working=True
            
        d.save()         
    return redirect('/emp/home')


def add_salary(request):
    if request.method=="POST":
        salary_holder_name=request.POST.get('salary_holder_name')
        salary_holder_id=request.POST.get('salary_holder_id')
        salary_account_no=request.POST.get('salary_account_no')
        salary_date=request.POST.get('salary_date')
        salary_amount=request.POST.get('salary_amount')
        
        s=Salary()
        
        s.name=salary_holder_name
        s.salary_id=salary_holder_id
        s.account_no=salary_account_no
        s.date=salary_date
        s.amount=salary_amount
        
        s.save()
        
        
        return redirect('/emp/home/')
        
    
    return render(request,'emp/add_salary.html',{})

def delete_salary(request,salary_id):
    salary=Salary.objects.get(pk=salary_id)
    salary.delete()
    return redirect('/emp/home/')

def update_salary(request,salary_id):
    salary=Salary.objects.get(pk=salary_id)
    
    return render(request,'emp/update_salary.html',{
        'salary':salary
    })
    
def do_update_salary(request,salary_id):
    if request.method=="POST":
        salary_holder_name=request.POST.get('salary_holder_name')
        salary_holder_id=request.POST.get('salary_holder_id')
        salary_account_no=request.POST.get('salary_account_no')
        salary_date=request.POST.get('salary_date')
        salary_amount=request.POST.get('salary_amount')
        
        s=Salary.objects.get(pk=salary_id)
        
        s.name=salary_holder_name
        s.salary_id=salary_holder_id
        s.account_no=salary_account_no
        s.date=salary_date
        s.amount=salary_amount
        
        s.save()
        return redirect('/emp/home')
    
def leave_request(request):
    if request. method=='POST':
        leave_holder_name=request.POST.get('leave_holder_name')
        leave_id=request.POST.get('leave_id')
        leave_subject=request.POST.get('leave_subject')
        leaving_start_date=request.POST.get('leaving_start_date')
        leaving_end_date=request.POST.get('leaving_end_date')
        leave_apruval=request.POST.get('leave_apruval')
        
        l=Leave()
        
        l.name=leave_holder_name
        l.leave_id=leave_id
        l.subject=leave_subject
        l.start_date=leaving_start_date
        l.end_date=leaving_end_date
        if leave_apruval is None:
            l.apruval=False
        else:
            l.apruval=True
            
    
        
        l.save()
        
        
        return redirect('/emp/home/')
        
        
    return render(request,'emp/leave_request.html',{})


def delete_leave_request(request,leave_id):
    leave=Leave.objects.get(pk=leave_id)
    leave.delete()
    return redirect('/emp/home/')

def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,'emp/testimonials.html',{
        'testi':testi
    })
    

        
        