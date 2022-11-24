from django.shortcuts import render
from django.http import HttpResponse


def new_rec(request):
    with open('log.txt', 'a') as log:
        log.write("\n")
        log.write(request.GET['name'])
    
    return HttpResponse("Added successfully <form action = http://192.168.0.156/view> <button>OK</button> </form>")

def view(request):
    with open('log.txt', 'r') as log:
        lines = log.readlines()
    with open('log2.txt', 'w') as log:
        log.write(lines[0])    
    responce = ""
    for i in lines:
        responce += i
        responce += "<br>"
    responce += "<form action = http://192.168.0.156/new> <button>Add new</button> </form>"
    return HttpResponse(responce)
# Create your views here.
