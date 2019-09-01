from django.contrib.auth.forms import UserCreationForm
from django import forms
from calculator.models import StudentProfile, Result
from django.contrib.auth.models import User


class StudentCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class StudentBioForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['matric_no', 'department', 'faculty', 'level', 'sex']


class ComputeResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['course_code', 'course_title', 'course_unit', 'course_type',
                  'total_score', 'session', 'semester']
