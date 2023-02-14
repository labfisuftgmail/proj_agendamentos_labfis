from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from .models import Area, Arquivo, Experimento
from .forms import ArquivoForm

# Create your views here.
def list_view(request):
    context = {}

    if request.method == "GET":
        context['experimentos'] = Experimento.objects.all()
        return render(request, 'experimentos/list_view.html', context)

def detail_view(request, id):
    context = {}

    if request.method == "GET":
        context['experimento'] = Experimento.objects.get(id=id)
        return render(request, 'experimentos/detail_view.html', context)
