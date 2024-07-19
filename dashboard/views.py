from django.shortcuts import render
from models import TaskData
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	if request.method == 'POST':
		TaskName = request.POST['']
		TaskPoints = request.POST['']
		TaskForm = TaskData(TaskName=TaskName, TaskPoints=TaskPoints, UserName=User.username)
		TaskForm.save()
	LoadTaskData = TaskData.objects.all()
	
	return render(request, 'dashboard/base.html')

def profi(request):
	return render(request, 'dashboard/profile.html')