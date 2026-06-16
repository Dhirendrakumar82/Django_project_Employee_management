from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/list.html', {
        'departments': departments
    })


def department_add(request):
    form = DepartmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('department_list')

    return render(request, 'department/add.html', {
        'form': form
    })


def department_edit(request, id):
    department = get_object_or_404(Department, id=id)

    form = DepartmentForm(
        request.POST or None,
        instance=department
    )

    if form.is_valid():
        form.save()
        return redirect('department_list')

    return render(request, 'department/add.html', {
        'form': form
    })


def department_delete(request, id):
    department = get_object_or_404(
        Department,
        id=id
    )

    department.delete()

    return redirect('department_list')


# from django.shortcuts import render, redirect
# from .models import Department
# from .forms import DepartmentForm

# def department_list(request):
#     departments = Department.objects.all()
#     return render(request,
#                  'department/list.html',
#                  {'departments': departments})

# def department_add(request):
#     form = DepartmentForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('department_list')

#     return render(request,
#                  'department/add.html',
#                  {'form': form})