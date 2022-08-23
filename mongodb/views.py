from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from .utils import connect_mongodb
from bson.objectid import ObjectId
import datetime

# Create your views here.
def home(request):
    if request.method == "GET":
       #employees = Employee.objects.all()
       employees = connect_mongodb("read","", {})
       context = {"employees" : employees}

       return render(request,"home.html",context)

def create(request):

    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
           emp_dict = {}
           emp_dict["first_name"] = form.cleaned_data["first_name"]
           emp_dict["last_name"] = form.cleaned_data["last_name"]
           emp_dict["email_id"] = form.cleaned_data["email_id"]
           emp_dict["phone"] = str(form.cleaned_data["phone"])
           emp_dict["address"] = form.cleaned_data["address"]
           emp_dict["city"] = form.cleaned_data["city"]
           emp_dict["state"] = form.cleaned_data["state"]
           emp_dict["zipcode"] = form.cleaned_data["zipcode"]
           emp_dict["date_added"] = datetime.datetime.now()
           connect_mongodb("create", "", emp_dict)
           return redirect('home')
        else:
            print("Form is not valid.")
            print(form.errors)

    context = {'form': form}
    return render(request, "create.html", context)

def update(request, id):

    obj_emp = Employee.objects.get(_id=ObjectId(id))
    form = EmployeeForm(instance=obj_emp)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=obj_emp)
        if form.is_valid():
            emp_dict = {}
            emp_dict["first_name"] = form.cleaned_data["first_name"]
            emp_dict["last_name"] = form.cleaned_data["last_name"]
            emp_dict["email_id"] = form.cleaned_data["email_id"]
            emp_dict["phone"] = str(form.cleaned_data["phone"])
            emp_dict["address"] = form.cleaned_data["address"]
            emp_dict["city"] = form.cleaned_data["city"]
            emp_dict["state"] = form.cleaned_data["state"]
            emp_dict["zipcode"] = form.cleaned_data["zipcode"]
            emp_dict["date_added"] = datetime.datetime.now()
            connect_mongodb("update", id , emp_dict)
            return redirect("home")
        else:
            print("Form is not valid.")
            print(form.errors)

    context = {'form': form}
    return render(request, "update.html", context)

def delete(request, id):
    if request.method == "GET":
       employee = connect_mongodb("get", id, {})
       context = {'employee': employee}
       return render(request,"delete.html", context)

    if request.method == "POST":
       connect_mongodb("delete", id, {})
       return redirect("home")
