from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_api_faq_list():
    client = APIClient()
    response = client.get("/faq_app/faq-list/", HTTP_Accept="application/json")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)


