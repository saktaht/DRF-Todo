from django.urls import path

from .views import TodoCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("todos/", TodoCreateAPIView.as_view(), name="todo_create"),
    path("todos/<int:pk>/", TodoRetrieveUpdateDestroyAPIView.as_view(), name="todo_rud"),
]