from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    #check cheackbox values
    removepunc = request.POST.get('removepunc', 'off')
    Fullcaps = request.POST.get('Fullcaps', 'off')
    Newlineremover=request.POST.get('Newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check cheackbox is on
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(Fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            params = {'purpose': 'Change to Upper text', 'analyzed_text': analyzed}
        djtext = analyzed

    if (Newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
                params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
            params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed =0
        for  char in djtext:
            if char!=" ":
                analyzed=analyzed+1
            params = {'purpose': 'Number of chacter in Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc!="on" and spaceremover!="on" and Fullcaps!="on" and Newlineremover!="on" and charcount!="on"):
        return HttpResponse("ERROR")
    return render(request, 'analyze.html', params)

def AboutUs(request):
    return render(request,'AboutUs.html')