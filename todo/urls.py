from django.urls import path
from . import views
app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='create'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('<id>/update/', views.todo_update),
    path('<id>/delete/', views.todo_delete),
    path('register/', views.register),
    path('login/', views.loginup, name='login'),
    path('logout/', views.logout_user),
    
]