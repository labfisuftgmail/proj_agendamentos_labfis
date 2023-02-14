from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Curso, Docente
from .forms import CursoForm, DocenteForm

# Create your views here.
def detail_view(request):
    context = {}

    curso_form = CursoForm()
    docente_form = DocenteForm()

    if request.method == "POST":
        if request.POST['label']=='CursoForm':
            form = CursoForm(request.POST or None, request.FILES or None)
        elif request.POST['label']=='DocenteForm':
            form = DocenteForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados inseridos com sucesso!')
            return redirect('docentes:detail_view')


    context['cursos'] = Curso.objects.all()
    context['docentes'] = Docente.objects.all()
    context['curso_form'] = curso_form
    context['docente_form'] = docente_form

    return render(request, 'docentes/detail_view.html', context)

def update_view(request, obj, id):

    if request.method == "GET":
        context = {}

        if obj == 'curso':
            curso = Curso.objects.get(id=id)
            form = CursoForm(instance=curso)
        elif obj == 'docente':
            docente = Docente.objects.get(id=id)
            form = DocenteForm(instance=docente)

        context['obj'] = obj
        context['form'] = form

        return render(request, 'docentes/update_view.html', context)

    if request.method == "POST":
        if request.POST['label']=='CursoForm':
            curso = Curso.objects.get(id=id)
            form = CursoForm(request.POST or None, request.FILES or None, instance=curso)

        if request.POST['label']=='DocenteForm':
            docente = Docente.objects.get(id=id)
            form = DocenteForm(request.POST or None, request.FILES or None, instance=docente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Dados alterados com sucesso!')
            return redirect('docentes:detail_view')


def delete_view(request, obj, id):
    if obj == 'curso':
        obj = Curso.objects.get(id=id)
    elif obj == 'docente':
        obj = Docente.objects.get(id=id)

    obj.delete()
    messages.success(request, 'Dados excluídos com sucesso!')
    return redirect('docentes:detail_view')
    
    