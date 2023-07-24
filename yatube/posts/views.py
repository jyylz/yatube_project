from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком групп
def group_list(request):
    return HttpResponse('Список мороженого')

# Страница с информацией о постах группы
def group_posts(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')