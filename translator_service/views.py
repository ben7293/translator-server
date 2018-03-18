#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from langdetect import detect
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator
from .models import Translations
import json

@csrf_exempt
def translate(request):
    print(request.body)
    original_text = json.loads(request.body.decode('utf-8'))['Text']

    lang = detect(original_text)
    # fire a API request to translate on Google
    translator = Translator()
    translatedString = translator.translate(original_text, src=lang).text
    # insert into database
    translation = Translations(original_text=original_text, original_lang=lang, translation=translatedString)
    translation.save()
    # return the result in JSON format
    return JsonResponse({"original_text": original_text, "original_lang": lang, "translation": translatedString}, json_dumps_params={'ensure_ascii':False})