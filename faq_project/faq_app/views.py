from django.shortcuts import render, redirect
from django.http import JsonResponse
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

# def faq_list(request):
#     lang = request.GET.get('lang', 'en')
#     faqs = FAQ.objects.all()
#     translated_faqs = [faq.get_translation(lang) for faq in faqs]
#     return render(request, 'faq_app/faq_list.html', {'faqs': translated_faqs})

# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import FAQ

def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    translated_faqs = [faq.get_translation(lang) for faq in faqs]
    
    # Check the 'Accept' header for JSON response
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse(translated_faqs, safe=False, json_dumps_params={'ensure_ascii': False})
    
    # Fallback to HTML rendering if Accept header is not 'application/json'
    return render(request, 'faq_app/faq_list.html', {'faqs': translated_faqs})


def index(request):
    return render(request, "faq_app/index.html") 