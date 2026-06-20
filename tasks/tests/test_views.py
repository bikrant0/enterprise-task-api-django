import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from tasks.models import Task

User = get_user_model()

@pytest.mark.django_db
def test_unauthenticated_user_cannot_get_tasks():
    #1.ARRANGE
    client = APIClient()
    url = '/api/tasks/'
    
    #2. ACT
    response = client.get(url)
    
    #3. ASSERT
    assert response.status_code == 401 
    
    
@pytest.mark.django_db    
def test_authenticated_user_can_get_tasks():
    # 1.ARRANGE
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='password123')
    
    Task.objects.create(title="API Task", user=user)
    
    client.force_authenticate(user=user)
    url = '/api/tasks/'
    
    # 2.ACT 
    response = client.get(url)
    
    # 3.ARRANGE
    assert response.status_code == 200 
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['title'] == "API Task"