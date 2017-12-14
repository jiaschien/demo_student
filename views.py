# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        cleaned_data = form.cleaned_data
        student = Student()
        student.name = cleaned_data['name']
        student.sex = cleaned_data['sex']
        student.email = cleaned_data['email']
        student.phone = cleaned_data['phone']
        student.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context={'students': students})