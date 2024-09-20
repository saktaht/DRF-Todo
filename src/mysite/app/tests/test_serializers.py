import pytest
from app.serializers import TodoSerializer
from app.models import Todo


# シリアライズできているかテスト
@pytest.mark.django_db
def test_todo_serializer_valid_data():
    todo = Todo.objects.create(title="Test Task")
    # シリアライズしている ← pythonオブジェクトをjsonに変換
    serializer = TodoSerializer(instance=todo)
    data = serializer.data

    assert data["title"] == "Test Task"
    assert "id" in data

# タイトルがからの場合のテスト
@pytest.mark.django_db
def test_todo_serializer_invalid_data():
    invalid_data = {"title": ""}
    serializer = TodoSerializer(data=invalid_data)

    assert not serializer.is_valid() 
    assert "title" in serializer.errors

# オブジェクトがデータベースに正しく保存され、タイトルが期待通りであることを確認
@pytest.mark.django_db
def test_todo_serializer_create():
    valid_data = {"title": "New Task"}
    serializer = TodoSerializer(data=valid_data)

    assert serializer.is_valid()
    todo = serializer.save()
    
    assert todo.title == "New Task"
    assert Todo.objects.count() == 1