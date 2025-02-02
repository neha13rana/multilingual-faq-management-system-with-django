from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_faq(request):
    return redirect("faq_home") 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("faq_app/", include("faq_app.urls")),
    path("", redirect_to_faq, name="home"),
]

