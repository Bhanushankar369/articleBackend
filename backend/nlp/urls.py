from django.contrib import admin
from django.urls import path
from nlp.views import summarize

urlpatterns = [
    path('summarize/', summarize, name='summarize'),
]
