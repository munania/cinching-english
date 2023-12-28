from django.shortcuts import render
import requests

# Create your views here.

def freeDict(request):

    if request.method == 'POST':
        word = request.POST.get('word', '')
        if word:
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
            response = requests.get(url).json()
        
        else:
            response = None

    else:
        response = None

    context = {'response': response}

    return render(request, 'freeDict/freedict.html', context=context)