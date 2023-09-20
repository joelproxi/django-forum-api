from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

import pytest

class TestCreateQuestions:
    def test_if_user_is_anonymous_retruns_401(self):
        client = APIClient()
        response = client.post('/forum/questions/', {
            "title": 'a',
            "content": "a",
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    @pytest.mark.django_db
    def test_if_data_is_invalid_retruns_400(self):
        client = APIClient()
        client.force_authenticate(user=User())
        response = client.post('/forum/questions/', {
            "title": 'a',
            "content": "a",
        }, )
        print(response)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
