import pytest
from app.models import Todo


@pytest.mark.django_db
def test_app_view_todos(client):
    # テスト用のリクエストオブジェクトを作成
    response = client.get("/app/todos/")
    # レスポンスのステータスコードが200であることを確認
    assert response.status_code == 200

@pytest.mark.django_db
def test_app_view_todos_pk(client):
    # 上と同じ動き
    todo = Todo.objects.create(title="Test")
    response = client.get(f"/app/todos/{todo.pk}/")
    assert response.status_code == 200