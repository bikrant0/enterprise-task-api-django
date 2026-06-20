import pytest
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

@pytest.mark.django_db
def test_task_creation():
    # 1. ARRANGE
    user = User.objects.create_user(username='testuser', password='testpass123')
    
    # 2. ACT
    task = Task.objects.create(
        title="My First Test Task",
        description="Testing is awesome",
        status="TODO",
        user=user
    )
    
    # 3. ASSERT
    assert task.title == "My First Test Task"
    assert task.user.username == "testuser"
    assert Task.objects.count() == 1