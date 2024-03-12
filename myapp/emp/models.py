from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    department=models.CharField(max_length=10)
    working=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
    
class Department(models.Model):
     name=models.CharField(max_length=200)
     department_id=models.CharField(max_length=200)
     phone=models.CharField(max_length=10)
     working=models.BooleanField(default=True)
     
class Salary(models.Model):
    name=models.CharField(max_length=200)
    salary_id=models.CharField(max_length=200)
    account_no=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    
class Leave(models.Model):
    name=models.CharField(max_length=200)
    leave_id=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    start_date=models.CharField(max_length=200)
    end_date=models.CharField(max_length=200)
    apruval=models.BooleanField(default=True)
    
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)
    
    def __str__(self):
        return self.testimonial
    
    
        
    
    
    
    
    
        
    
    
    
         
     
        
