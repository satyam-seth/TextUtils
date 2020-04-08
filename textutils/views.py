# I have created this file myself - Satyam Seth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse('<h1>Please select your operation and try again.</h1>')
    return render(request, 'analyze.html', params)
