from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
# @csrf_exempt
# def home(request):
# 	print("I am in home")
# 	if request.method == 'POST':
# 		print(" I am in post request")
# 		print("This is request post thing",request.POST)
# 		# TaskName = request.POST['TaskName']
# 		# TaskPoints = request.POST['TaskPoints']
# 		# print(TaskName, TaskPoints, request.POST['task-name'])
# 		# TaskForm = TaskData(TaskName=TaskName, TaskPoints=TaskPoints, Status="Pending")
# 		# TaskForm.save()
# 		# print(TaskName, TaskForm)
# 	LoadTaskData = TaskData.objects.all()

# 	return render(request, 'dashboard/base.html')


def index(request):
    tasks = Task.objects.all()
    total_points = sum(task.points for task in tasks if task.is_completed)
    return render(request, 'dashboard/base.html', {'tasks': tasks, 'total_points': total_points})

def add_task(request):
    if request.method == 'POST':
        name = request.POST['task_name']
        points = int(request.POST['task_points'])
        Task.objects.create(name=name, points=points, UserName=request.user)
    return redirect('dashboard-home')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard-home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.is_completed:
        task.points = -task.points
    task.delete()
    return redirect('dashboard-home')


def profi(request):
	return render(request, 'dashboard/profile.html')