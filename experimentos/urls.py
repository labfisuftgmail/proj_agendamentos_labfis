from django.urls import path
from . import views

app_name = 'experimentos'

urlpatterns = [
    path('experimentos/', views.list_view, name='list_view'),
    path('experimentos/<int:id>', views.detail_view, name='detail_view'),
]