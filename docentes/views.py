from django.shortcuts import render

# Create your views here.
def detail_view(request):
    return render(request, 'docentes/detail_view.html')