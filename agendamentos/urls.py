from django.urls import path
from . import views

app_name = 'agendamentos'

urlpatterns = [
    path('', views.detail_view, name='detail_view'),
]