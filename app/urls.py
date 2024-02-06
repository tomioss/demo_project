from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task_viewset')


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:id>/', views.toggle_task, name='toggle_task'),
    path('api/', include(router.urls)),
]
