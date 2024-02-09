from django.http import HttpResponseRedirect
from django.shortcuts import render
from circuits.models import Circuit
from descriptions.models import Description

def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode'] 
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home_view(request):
    qs= Circuit.objects.all()
    print(qs)
    obj = Circuit.objects.get(id=1)  # es la referencia del objeto padre
    descriptions = obj.descriptions  # por una property se trata como que fuera un campo

    context = {
        'qs': qs,
        'obj': obj,
        'descriptions': descriptions,
    }
    return render(request, 'main.html', context)
