from django.shortcuts import render, redirect
from django.http import JsonResponse
from googletrans import Translator
from .forms import FAQForm
from .models import FAQ

def submit_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            
            if not question or not answer:
                return JsonResponse({'error': 'Question and answer cannot be empty'}, status=400)
            
            translator = Translator()
            try:
                translated_question = translator.translate(question, src='en', dest='bn').text
                translated_answer = translator.translate(answer, src='en', dest='bn').text
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

            faq = form.save(commit=False)
            faq.translated_question = translated_question
            faq.translated_answer = translated_answer
            faq.save()

            return redirect('faq_list')
    else:
        form = FAQForm()

    return render(request, 'faq_app/submit_faq.html', {'form': form})

def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    translated_faqs = [faq.get_translation(lang) for faq in faqs]

    if request.headers.get('Accept') == 'application/json':
        return JsonResponse(translated_faqs, safe=False, json_dumps_params={'ensure_ascii': False})
    
    return render(request, 'faq_app/faq_list.html', {'faqs': translated_faqs})


def index(request):
    return render(request, "faq_app/index.html") 