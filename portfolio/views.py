from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


# Vista para el formulario de Project
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Cambia 'project_list' al nombre de la vista donde quieres redirigir después de guardar
    else:
        form = ProjectForm()
    return render(request, 'formularios/form_project.html', {'form': form})