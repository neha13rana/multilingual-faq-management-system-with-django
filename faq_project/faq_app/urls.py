from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_faq, name='submit_faq'),
    path('faq-list/', views.faq_list, name='faq_list'),
     path("", views.index, name="faq_home"),
]
