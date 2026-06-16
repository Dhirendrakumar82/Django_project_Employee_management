from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def dashboard(request):

    total_employees = Employee.objects.count()

    context = {
        'total_employees': total_employees,
    }

    return render(request, 'dashboard.html', context)


def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employee/employee_list.html',
        {'employees': employees}
    )


def employee_add(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employee/employee_form.html',
        {'form': form}
    )


def employee_edit(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employee/employee_form.html',
        {'form': form}
    )


def employee_delete(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    employee.delete()

    return redirect('employee_list')



# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Employee
# from .forms import EmployeeForm

# def dashboard(request):
#     total_employees = Employee.objects.count()

#     context = {
#         'total_employees': total_employees
#     }

#     return render(request, 'dashboard.html', context)

# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'employee/list.html',
#                   {'employees': employees})

# def employee_add(request):
#     form = EmployeeForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('employee_list')

#     return render(request,
#                   'employee/add.html',
#                   {'form': form})

# def employee_update(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)

#     form = EmployeeForm(
#         request.POST or None,
#         instance=employee
#     )

#     if form.is_valid():
#         form.save()
#         return redirect('employee_list')

#     return render(request,
#                   'employee/add.html',
#                   {'form': form})

# def employee_delete(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     employee.delete()
#     return redirect('employee_list')