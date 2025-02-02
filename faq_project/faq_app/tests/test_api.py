from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from faq_app.models import FAQ


@pytest.mark.django_db
def test_api_faq_list():
    client = APIClient()
    response = client.get(reverse('faq_list'), HTTP_Accept="application/json")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    response = client.get(reverse('faq_list') + "?lang=bn", HTTP_Accept="application/json")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)

@pytest.mark.django_db
def test_api_submit_faq():
    client = APIClient()

    data = {
        "question": "What is Django?",
        "answer": "Django is a high-level Python Web framework."
    }

    url = reverse('submit_faq')  
    response = client.post(url, data, format='json')

    assert response.status_code == 200 
 
@pytest.mark.django_db
def test_api_faq_list_with_lang_param():
    client = APIClient()
    faq_en = FAQ.objects.create(question="What is Django?", answer="Django is a high-level Python Web framework.")
    faq_bn = FAQ.objects.create(question="জ্যাঙ্গো কী?", answer="জ্যাঙ্গো একটি উচ্চ-স্তরের পাইথন ওয়েব ফ্রেমওয়ার্ক") 

    response = client.get(reverse('faq_list') + "?lang=en", HTTP_Accept="application/json")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 2  
    assert response_data[0]['question'] == "What is Django?"

    response = client.get(reverse('faq_list') + "?lang=bn", HTTP_Accept="application/json")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) == 2 
    assert response_data[0]['question'] == "জ্যাঙ্গো কী?" 
