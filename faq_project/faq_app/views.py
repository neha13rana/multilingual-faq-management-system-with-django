from django.shortcuts import render, redirect
from .forms import FAQForm
from .models import FAQ

def submit_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faq_app/submit_faq.html', {'form': form})

def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    translated_faqs = [faq.get_translation(lang) for faq in faqs]
    return render(request, 'faq_app/faq_list.html', {'faqs': translated_faqs})

def index(request):
    return render(request, "faq_app/index.html") 