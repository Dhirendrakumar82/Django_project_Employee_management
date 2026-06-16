from django.shortcuts import render, redirect
from .models import Payroll, Employee


# Payroll List
def payroll_list(request):
    payrolls = Payroll.objects.all()

    return render(
        request,
        'payroll/payroll_list.html',
        {'payrolls': payrolls}
    )


# Add Payroll
def payroll_add(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        employee = Employee.objects.get(
            id=request.POST.get('employee')
        )

        salary = float(
            request.POST.get('salary', 0) or 0
        )

        bonus = float(
            request.POST.get('bonus', 0) or 0
        )

        deduction = float(
            request.POST.get('deduction', 0) or 0
        )

        net_salary = salary + bonus - deduction

        Payroll.objects.create(
            employee=employee,
            salary=salary,
            bonus=bonus,
            deduction=deduction,
            net_salary=net_salary
        )

        return redirect('payroll_list')

    return render(
        request,
        'payroll/payroll_add.html',
        {'employees': employees}
    )




# from .models import Payroll, Employee
# from django.shortcuts import render, redirect

# def payroll_list(request):
#     payrolls = Payroll.objects.all()
#     return render(request,
#                   'payroll/payroll_list.html',
#                   {'payrolls': payrolls})


# def payroll_add(request):

#     employees = Employee.objects.all()

#     if request.method == "POST":

#         employee = Employee.objects.get(
#             id=request.POST['employee']
#         )

#         salary = request.POST['salary']
#         bonus = request.POST['bonus']
#         deduction = request.POST['deduction']

#         net_salary = (
#             float(salary)
#             + float(bonus)
#             - float(deduction)
#         )

#         Payroll.objects.create(
#             employee=employee,
#             salary=salary,
#             bonus=bonus,
#             deduction=deduction,
#             net_salary=net_salary
#         )

#         return redirect('payroll_list')

#     return render(
#         request,
#         'payroll/payroll_add.html',
#         {'employees': employees}
#     )



# # from django.shortcuts import render, redirect
# # from .models import Payroll
# # from .forms import PayrollForm

# # def payroll_list(request):

# #     payrolls = Payroll.objects.all()

# #     return render(
# #         request,
# #         'payroll/list.html',
# #         {'payrolls': payrolls}
# #     )

# # def payroll_add(request):

# #     form = PayrollForm(
# #         request.POST or None
# #     )

# #     if form.is_valid():

# #         payroll = form.save(
# #             commit=False
# #         )

# #         payroll.net_salary = (
# #             payroll.salary
# #             + payroll.bonus
# #             - payroll.deduction
# #         )

# #         payroll.save()

# #         return redirect(
# #             'payroll_list'
# #         )

# #     return render(
# #         request,
# #         'payroll/payroll_add.html',
# #         {'form': form}
# #     )