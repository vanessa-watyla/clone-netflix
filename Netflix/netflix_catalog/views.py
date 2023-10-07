from django.shortcuts import render

def index(request):
    return render(request, 'nome_do_aplicativo/index.html')

