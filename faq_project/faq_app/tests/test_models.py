import pytest
from faq_app.models import FAQ
from unittest.mock import patch

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."

@pytest.mark.django_db
@patch("faq_app.models.FAQ.translate")
def test_faq_translation(mock_translate):
    mock_translate.return_value = "नमस्ते" 
    faq = FAQ.objects.create(question="Hello", answer="World")
    translated_hi = faq.translate(faq.question, 'hi')
    assert isinstance(translated_hi, str)
    assert translated_hi == "नमस्ते"
