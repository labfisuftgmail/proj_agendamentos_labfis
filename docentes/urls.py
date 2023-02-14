from django.urls import path
from . import views

app_name = 'docentes'

urlpatterns = [
    path('docentes/', views.detail_view, name='detail_view'),
    path('editar/<str:obj>/<int:id>', views.update_view, name='update_view'),
    path('excluir/<str:obj>/<int:id>', views.delete_view, name='delete_view'),
]