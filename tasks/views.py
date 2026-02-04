from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    user = request.user
    if user.is_staff:
        tasks = Task.objects.all() 
    else:
        tasks = Task.objects.filter(user=user)
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, id):
    user = request.user
    
    task = Task.objects.filter(id=id).first()
    if not task:
        return Response({'message': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if not user.is_staff and task.user != user:
        return Response({'message': 'You are not the owner of this task'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
    user = request.user
    
    task = Task.objects.filter(id=id).first()
    if not task:
        return Response({'message': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if not user.is_staff and task.user != user:
        return Response({'message': 'You are not the owner of this task'}, status=status.HTTP_401_UNAUTHORIZED)
    
    task.delete()
    return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)