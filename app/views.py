import csv
from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):

    employee=Employee.objects.order_by('first_name')
    return render(request,'home.html',{'list':employee})


def new_employee(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)

            employee.save()
            messages.success(request,'employee added successfuly')
        return redirect('home')

    else:
        form= NewEmployeeForm()

    return render(request, 'new_employee.html', {'form':form})




def singleEmployee(request,id):

    try:
        employee = Employee.objects.get(id = id)
    except DoesNotExist:
        raise Http404('no such item')
    return render(request,"singleEmployee.html", {"employee":employee})


def updateEmployee(request,pk):

    employee = get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        form =NewEmployeeForm(request.POST,instance=employee)

        try:
          if form.is_valid():
            employee=form.save(commit=False)
            employee.save()
            messages.success(request,'employee recods has been updated successfuly')
            return redirect(home)
        except Exception as e:

            HttpResponse(request, 'your records are not saved')
    else :
        form = NewEmployeeForm(instance=employee)

        return render(request, 'updateEmployee.html', {'form':form,"employee":employee})


def delete_employee(request, id):


        employee = Employee.objects.get(pk=id)

        employee.delete()
        messages.warning(request,'employee recods deleted')
        return redirect(home)

        return render(request, 'updateEmployee.html', {'employee': employee})


def confirm_delete(request,id):

    employee = Employee.objects.get(pk=id)
    return render(request,'delete.html',{'employee':employee})



def search_results(request):

    if 'department' in request.GET and request.GET["department"]:
        search_term = request.GET.get("department")
        searched_department = Employee.search_by_department(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"employee": searched_department})

    else:
        message = "You haven't searched for any department"
        return render(request, 'search.html',{"message":message})

def download_csv(request):
    '''
    function that exports html table to csv
    '''
    items = Employee.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Deposition']= 'attachment;filename="table.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['first_name','last_name','Salary','department'])
    for obj in items:
        writer.writerow([obj.first_name,obj.last_name,obj.Salary,obj.department])
    return response
