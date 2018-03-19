from django.http import HttpResponse, JsonResponse
from langdetect import detect
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator
from .models import Translations
import json

@csrf_exempt
def translate(request):
    original_text = json.loads(request.body.decode('utf-8'))['Text']
    # fire a API request to translate on Google
    translator = Translator()
    translated = translator.translate(original_text)
    # insert into database
    translation = Translations(original_text=original_text, original_lang=translated.src, translation=translated.text)
    translation.save()
    # return the result in JSON format
    return JsonResponse({"original_text": original_text, "original_lang": translated.src, "translation": translated.text}, json_dumps_params={'ensure_ascii':False})

def getTranslationRecords(request):
	return JsonResponse(list(Translations.objects.values()), safe=False)    