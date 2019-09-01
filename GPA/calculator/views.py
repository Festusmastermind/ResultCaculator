from django.shortcuts import render, redirect
from .forms import StudentCreationForm, StudentBioForm
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Result
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ComputeResultForm


# View functions to power the users request

def dashboard(request):
    user = request.user
    current_user = user
    result_list = current_user.result_set.all()
    if result_list:
        Twgp = 0
        Tcu = 0
        for result in result_list:
            Tcu = int(result.course_unit) + Tcu
            Twgp = int(result.course_unit)*int(result.grade_pt) + Twgp
        Gpa = Twgp/Tcu
        Current_Gpa = round(Gpa, 2)
        print(Current_Gpa)
        context = {
            'result_list': result_list,
            'Tcu': Tcu,
            'Twgp': Twgp,
            'Gpa': Gpa,
            'Current_Gpa': Current_Gpa
        }
        return render(request, 'calculator/dashboard.html', context)
    else:
        messages.warning(request, f'You have no results yet!!')
        return render(request, 'calculator/dashboard.html',)


def createAcct(request):
    if request.method == 'POST':
        create_form = StudentCreationForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f'Account Creation Successful')
            return redirect('bio_reg')
        else:
            messages.warning(request, 'Please fill in the appropriate Data')
    else:
        create_form = StudentCreationForm()

    context = {
        'create_form': create_form
    }
    return render(request, 'calculator/create_acct.html', context)


# This is also not working....unless the users login first the data  cant be bind.
# Which is why we need to define our own custom user to hold specific authentication data.
def bio_reg(request):
    if request.method == 'POST':
        bio_form = StudentBioForm(request.POST, instance=request.user.studentprofile)
        if bio_form.is_valid():
            binding = bio_form.save(commit=False)
            binding.user = request.user
            binding.save()
            return redirect('login')
        else:
            messages.warning(request, f'Please provide valid data')
    else:
        bio_form = StudentBioForm()
    # context = {
    #     'bio_form': bio_form
    # }
    return render(request, 'calculator/bio_reg.html', {'bio_form': bio_form})

@login_required
def myprofile(request):
    if not request.user.is_authenticated():
        return render(request, 'calculator/login.html')  # its not displaying form
    else:
        return render(request, 'calculator/profile.html')

@login_required
def add_result(request):
    if request.method == 'POST':
        add_form = ComputeResultForm(request.POST)
        if add_form.is_valid():
            result = add_form.save(commit=False)
            if result.total_score >=70 and result.total_score <= 100:
                result.grade_pt = 5
            elif result.total_score >=60 and result.total_score <= 69:
                result.grade_pt = 4
            elif result.total_score >=50 and result.total_score <= 59:
                result.grade_pt = 3
            elif result.total_score >=45 and result.total_score <= 49:
                result.grade_pt = 2
            elif result.totla_score >=0 and result.total_score <= 44:
                result.grade_pt = 0
            result.student = request.user
            result.save()
            messages.success(request, f'Result Added Succesfully')
            return redirect('load_result')
        else:
            messages.warning(request, f'Please fill in Valid Data')
    else:
        add_form = ComputeResultForm()
    return render(request, 'calculator/addresult.html', {'add_form': add_form})

# class ResultCreateView(LoginRequiredMixin, CreateView):
#     model = Result
#     template_name = 'calculator/addresult.html'
#     fields = ['course_code', 'course_title', 'course_unit', 'course_type',
#               'total_score', 'grade_pt', 'session', 'semester']
#     success_url = reverse_lazy('load_result')
#
#     def form_valid(self, form):
#         form.instance.student = self.request.user
#         return super().form_valid(form)


# Calculating the Gpa and Cgpa for both semesters......
# The view scope entails the cgpa and gpa from 100 to 400 level
@login_required
def load_result(request):
    user = request.user
    current_user = user
    result_list = current_user.result_set.all()
    if result_list:
        Twgp1 = 0 
        Tcu1 = 0
        Twgp2 = 0
        Tcu2 = 0
        for result in result_list:
            if result.semester == '1st Semester':
                Tcu1 = int(result.course_unit) + Tcu1
                Twgp1 = int(result.course_unit)*int(result.grade_pt) + Twgp1
            elif result.semester == '2nd Semester':
                Tcu2 = int(result.course_unit) + Tcu2
                Twgp2 = int(result.course_unit)*int(result.grade_pt) + Twgp2
        Gpa = Twgp1/Tcu1
        Current_Gpa = round(Gpa, 2)
        Cgpa = (Twgp1+Twgp2)/(Tcu1+Tcu2)
        Current_Cgpa = round(Cgpa, 2)
        print(Current_Gpa)
        print(Current_Cgpa)
        context = {
            'result_list': result_list,
            'Current_Gpa': Current_Gpa,
            'Current_Cgpa': Current_Cgpa
        }
        return render(request, 'calculator/result_list.html', context)
    else:
        context = {
            'error_message': 'Add result for computation',
        }
        return render(request, 'calculator/result_list.html', context)












# @login_required
# def load_result(request):
#     user = request.user
#     current_user = user
#     result_list = current_user.result_set.all()
#     if result_list:
#         Twgp = 0
#         Tcu = 0
#         for result in result_list:
#             Tcu = int(result.course_unit) + Tcu
#             Twgp = int(result.course_unit)*int(result.grade_pt) + Twgp
#         Gpa = Twgp/Tcu
#         Current_Gpa = round(Gpa, 2)
#         print(Current_Gpa)
#         context = {
#             'result_list': result_list,
#             'Tcu': Tcu,
#             'Twgp': Twgp,
#             'Gpa': Gpa,
#             'Current_Gpa': Current_Gpa
#         }
#         return render(request, 'calculator/result_list.html', context)
#     else:
#         context = {
#             'error_message': 'Add result for computation',
#         }
#         return render(request, 'calculator/result_list.html', context)



