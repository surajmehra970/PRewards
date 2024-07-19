from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='dashboard-home'),
    path('profile/',views.profi,name='profile')

]