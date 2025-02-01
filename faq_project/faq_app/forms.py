from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget()) 
    question_hi = forms.CharField(widget=forms.Textarea, required=False)
    question_bn = forms.CharField(widget=forms.Textarea, required=False)
    answer_hi = forms.CharField(widget=CKEditorWidget(), required=False)
    answer_bn = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn']
