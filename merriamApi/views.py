from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    if request.method == 'POST':
        word = request.POST.get('word', '')
        if word:
            response = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word +'?key=7').json()
        
        else:
            response = None

    else:
        response = None

    context = { 'response': response }
        
    return render(request, 'merriamApi/index.html', context=context)


    return render(request, 'merriamApi/index.html', context=context)