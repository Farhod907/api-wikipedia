from django.shortcuts import render
from django.http import JsonResponse
import wikipedia
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# from django.views.decorators.csrf import csrf_protect

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def Wikipedia(request):
    if request.method == 'POST':
        wikipedia.set_lang("uz")
        a = json.loads(request.body)
        info = wikipedia.summary(a['word'])
        return JsonResponse(info, safe=False)
    else:
        return JsonResponse('xatolik')
