from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1> Kim nen noi dau, gian du mat khon... </h1>")
    response.write(":((")
    return response