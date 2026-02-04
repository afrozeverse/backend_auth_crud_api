from django.urls import path
from .views import get_tasks,update_task,delete_task,create_task
import uuid
urlpatterns = [
    path('get-tasks/', get_tasks,name='getTasks'),
    path('create-task/', create_task,name='createTask'),
    path('update-task/<uuid:id>/', update_task,name='updateTask'),
    path('delete-task/<uuid:id>/', delete_task,name='deleteTask'),
]