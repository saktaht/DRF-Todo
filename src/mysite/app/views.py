from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

# 取得(一覧)、登録APIクラス
class TodoCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
# 取得(詳細)、更新、削除APIクラス
class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer