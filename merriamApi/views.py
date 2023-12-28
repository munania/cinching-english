from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    if request.method == 'POST':
        word = request.POST.get('word', '')
        if word:
            response = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word +'?key=ENTER_YOUR_OWN_KEY').json()
        
        else:
            response = None

    else:
        response = None

    context = { 'response': response }
        
    return render(request, 'merriamApi/index.html', context=context)



    # response = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/bed?key=ea2a1ebc-4e5f-48d4-8ecd-d967b603cc27').json()
    
    # context = { 'response': response }

    return render(request, 'merriamApi/index.html', context=context)