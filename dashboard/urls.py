from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-home'),
    path('add_task/', views.add_task, name='add_task'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('profile/',views.profi,name='profile')

]