from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm


def attendance_list(request):

    attendances = Attendance.objects.all()

    return render(
        request,
        'attendance/list.html',
        {'attendances': attendances}
    )


def attendance_add(request):

    form = AttendanceForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'attendance_list'
        )

    return render(
        request,
        'attendance/add.html',
        {'form': form}
    )


def attendance_edit(request, id):

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    form = AttendanceForm(
        request.POST or None,
        instance=attendance
    )

    if form.is_valid():

        form.save()

        return redirect(
            'attendance_list'
        )

    return render(
        request,
        'attendance/add.html',
        {'form': form}
    )


def attendance_delete(request, id):

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    attendance.delete()

    return redirect(
        'attendance_list'
    )