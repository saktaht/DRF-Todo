import pytest
from django.core.exceptions import ValidationError
from app.models import Todo


# pkが追加されてるかテスト
@pytest.mark.django_db
def test_todo_create():
    todo = Todo.objects.create(title="test")
    assert todo.title == "test"
    assert todo.pk is not None

# __str__の内容が正しいかテスト 
@pytest.mark.django_db
def test_todo_str():
    todo = Todo.objects.create(title="test")
    assert str(todo) == "test" 

# タイトルの最大文字数が100文字かテスト
@pytest.mark.django_db
def test_todo_title_max_length():
    todo = Todo(title="A" * 101)
    with pytest.raises(ValidationError):
        # モデルインスタンスをデータベースに保存する前に、full_clean()を呼び出して、データの整合性を確認
        todo.full_clean()