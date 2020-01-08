from django.shortcuts import render,redirect
from testapp.forms import EmployeeForm
from testapp.models import Employee
def homepage(request):
    form = EmployeeForm()
    emps = Employee.objects.all()
    return render(request,'testapp/homepage.html',{'form':form,'employees':emps})

def save_data(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/homepage.html',{'form':form})

def delete_employee(request,id):
    form = EmployeeForm()
    emp = Employee.objects.get(id=id)
    if emp:
        emp.delete()
        msg = 'Employee Deleted succesfully...'
    else:
        msg = 'Employee is not Present...'
    form = EmployeeForm()
    emps = Employee.objects.all()
    return render(request, 'testapp/homepage.html', {'form': form, 'employees': emps,'msg':msg})

def update_employee(request,id):
    emp  = Employee.objects.get(id=id)
    print(emp)
    # form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    return render(request,'testapp/update.html',{'emp':emp})