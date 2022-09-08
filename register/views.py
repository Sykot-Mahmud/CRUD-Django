from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    employee_list=Employee.objects.all()
    
    return render(request,'register/employee_list.html',{
        'employee_list':employee_list
    })

def employee_create(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'register/employee_form.html',context)


def employee_update(request,id):
    employee=Employee.objects.get(pk=id)
    form=EmployeeForm(instance=employee)
    
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'register/employee_form.html',context)


def employee_delete(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        employee.delete()
        return redirect('/')
    context={'employee':employee}
    return render(request,'register/delete.html',context)
  