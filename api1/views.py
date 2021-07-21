from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
# Create your views here.

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializers = TaskSerializers(tasks, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializers = TaskSerializers(tasks, many = False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializers(data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id = pk)
    serializers = TaskSerializers(instance= tasks, data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response("Successfully Deleted!")
