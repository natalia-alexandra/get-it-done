from django.urls import path
from task import views


urlpatterns = [
    # path('', views.todo_list, name='todo-list'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
]
