from django.urls import path
from . import views

app_name = 'experimentos'

urlpatterns = [
    path('experimentos/', views.detail_view, name='detail_view'),
]