from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def home_view(request):  
    return render(request,"testapp/home.html")


def model_view(request):
    all_data = Employee.objects.all()
    return render(request,"testapp/index.html",{'all_data':all_data})

from testapp.forms import EmployeeForm
def add_view(request):
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = EmployeeForm()
    return render(request,"testapp/add.html",{'form':form})


def home_view(request):
    return render(request,"testapp/home.html")