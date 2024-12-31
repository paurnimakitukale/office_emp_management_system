from django.shortcuts import render
from testapp.models import Employee
from django.contrib.auth.decorators import login_required
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


def base_view(request):
    return render(request,"testapp/base.html")

@login_required
def main_page_view(request):
    return render(request,'testapp/main.html')

@login_required
def java_views(request):
    return render(request,"testapp/java.html")

login_required
def python_views(request):
    return render(request,"testapp/python.html")

login_required
def aptitude_views(request):
    return render(request,"testapp/aptitude.html")


def logout_view(request):
    return render(request,'testapp/logout.html')

from testapp.forms import SignUpForm
def signup_view(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.set_password(user.password)
            user.save()
            print("user is created successfully")
    form = SignUpForm()        
    return render(request,"testapp/signup.html",{'form':form})