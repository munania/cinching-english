from django.shortcuts import render
import requests

# Create your views here.

def freeDict(request):
    response = requests.get(' https://api.dictionaryapi.dev/api/v2/entries/en/jury').json()

    context = {'response': response}

    return render(request, 'freeDict/freedict.html', context=context)