from django.urls import path
from . import views

app_name = 'docentes'

urlpatterns = [
    path('docentes/', views.detail_view, name='detail_view'),
]