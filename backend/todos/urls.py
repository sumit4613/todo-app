from django.urls import path, include
from .views import DetailTodo, ListTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name="todo-detail-view"),
    path('', ListTodo.as_view(), name="todo-list-view"),
]
