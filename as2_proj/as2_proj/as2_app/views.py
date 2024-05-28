# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ThesisProject, Supervisor, Student
from .forms import ThesisProjectForm, SupervisorForm, StudentForm

def home(request):
    return render(request, 'as2_app/home.html')

def projectlist(request):
    projects = ThesisProject.objects.all()
    context = {
        'articles': projects,
    }
    return render(request, 'as2_app/projectlist.html', context)

def about(request):
    return render(request, 'as2_app/about.html')

def project_details(request, pk):
    selected_project = get_object_or_404(ThesisProject, topic_num=pk)
    context = {
        'project': selected_project,
    }
    return render(request, 'as2_app/projectdetails.html', context)

def add_thessis(request):
    form = ThesisProjectForm()
    if request.method == 'POST':
        form = ThesisProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_forms')
    context = {'form': form}
    return render(request, 'as2_app/display_forms.html', context)

def add_supervisor(request):
    form = SupervisorForm()
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form': form}
    return render(request, 'as2_app/display_forms.html', context)

def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form': form}
    return render(request, 'as2_app/display_forms.html', context)

def update_thesis(request, pk):
    project = get_object_or_404(ThesisProject, topic_num=pk)
    if request.method == 'POST':
        form = ThesisProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ThesisProjectForm(instance=project)
    context = {'form': form}
    return render(request, 'as2_app/display_forms.html', context)

def delete_thesis(request, pk):
    project = get_object_or_404(ThesisProject, topic_num=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context = {'project': project}
    return render(request, 'as2_app/delete.html', context)

def display_forms(request):
    return render(request, 'as2_app/formss.html')


def studentlist(request):
    projects = Student.objects.all()
    context = {
        'articles': projects,
    }
    return render(request, 'as2_app/studentlist.html', context)
