import json
from django.http import HttpResponse
from get_word.models import Words
# Create your views here.
def get_my_word(request):
    try:
        _search = request.GET.get('word', 'default')
        _w = Words.objects.get(chine=_search)
        chine = _w.chine
        pinyin = _w.pinyin
        translate = _w.translate
        response_data = {}
        response_data['chine'] = chine
        response_data['pinyin'] = pinyin
        response_data['translate'] = translate
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except:
        return no_word(request)

    
def add_word(request):
    chine = request.GET.get('chine', 'default')
    pinyin = request.GET.get('pinyin', 'default')
    translate = request.GET.get('translate', 'default')
    try:
        _w = Words.objects.get(chine="ddadfsdfdsffs")
        return HttpResponse("Bar", content_type="application/json")
    except:  
        word = Words.objects.create(
            chine=chine,
            pinyin=pinyin,
            translate=translate
        )

        try:
            word.save()
            response_data = {}
            response_data['chine'] = chine
            response_data['pinyin'] = pinyin
            response_data['translate'] = translate
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        except:
            return HttpResponse("0", content_type="application/json")

    
def no_word(request):
    return HttpResponse("0", content_type="application/json")