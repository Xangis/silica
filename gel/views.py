from django.shortcuts import render_to_response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from tagging.fields import TagField, Tag
from tagging.models import TaggedItem, Tag
from models import SilicaPacket, Color, Language, Manufacturer

def index(request):
    packets = SilicaPacket.objects.all()
    return render_to_response('index.html', { 'packets': packets, })

def packet(request, id):
    try:
        packet = SilicaPacket.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('packet.html', { 'packet': packet, })

def colors(request):
    tags = Color.objects.all()
    return render_to_response('colors.html', { 'tags': tags, })

def color(request, color):
    try:
        col = Color.objects.get(slug=color)
    except ObjectDoesNotExist:
        raise Http404
    packets = SilicaPacket.objects.filter(print_color=col)
    return render_to_response('color.html', { 'packets': packets, 'color': col })

def languages(request):
    tags = Language.objects.all()
    return render_to_response('languages.html', { 'tags': tags, })

def language(request, language):
    try:
        lang = Language.objects.get(slug=language)
    except ObjectDoesNotExist:
        raise Http404
    packets = SilicaPacket.objects.filter(text_language=lang)
    return render_to_response('language.html', { 'packets': packets, 'language': lang })

def manufacturers(request):
    tags = Manufacturer.objects.all()
    return render_to_response('manufacturers.html', { 'tags': tags, })

def manufacturer(request, manufacturer):
    try:
        manufacturer = Manufacturer.objects.get(slug=manufacturer)
    except ObjectDoesNotExist:
        raise Http404
    packets = SilicaPacket.objects.filter(manufacturer_id=manufacturer)
    return render_to_response('manufacturer.html', { 'packets': packets, 'manufacturer': manufacturer})


