from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .forms import *
from registration.models import *


@login_required(login_url='admin:login')
def index(request):
    return render(request, "registration_index.html")


# Register student to the system
@login_required(login_url='admin:login')
def registration_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('registration:register')
    else:
        form = StudentForm
        return render(request, 'registration/registration_form.html', {'form': form})


# View a student registration
@login_required(login_url='admin:login')
def registration_detail(request, pk):
    data = get_object_or_404(Student, pk=pk)
    return render(request, 'registration/registration_detail.html', {'data': data})


# Edit a student registration
@login_required(login_url='admin:login')
def registration_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)
        return render(request, 'registration/registration_edit.html', {'form': form})


# View registration history
@login_required(login_url='admin:login')
def registration_history(request):
    data = Student.objects.order_by('date')
    return render(request, 'registration/registration_history.html', {'data': data})


# After successful registration, show success screen
@login_required(login_url='admin:login')
def registration_success(request):
    return render(request, 'registration/thank_you.html')