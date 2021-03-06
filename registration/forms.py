from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_number', 'first_name', 'last_name', 'program', 'year_level')