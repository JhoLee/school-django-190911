from django.shortcuts import render

# Create your views here.

def index(req):
    html = "<html><body> Hello !! </html></body>"
    return HttpResponse(html)