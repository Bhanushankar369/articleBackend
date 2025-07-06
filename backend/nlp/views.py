from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .nlpsummarize import summarize_text
# Create your views here.

@api_view(['GET', 'POST'])
def summarize(request):
    data = request.data
    text = data.get('url')
    result = summarize_text(text)
    return Response({"result": result}) 