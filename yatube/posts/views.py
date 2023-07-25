from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):   
    template = loader.get_template('ice_cream/index.html') 
    return render(template, request)

# Страница со списком групп
def group_list(request):
    return HttpResponse('Список мороженого')

# Страница с информацией о постах группы
def group_posts(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')