from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Домашня сторінка',
        'description': 'Це домашня сторінка проєкту DP_Rybalchenko.'
    }
    return render(request, 'home.html', context)


def resume(request):
    context = {
        'title': 'Резюме автора',
        'name': 'Данило Рибальченко',
        'experience': '5 років досвіду веб-розробки',
        'skills': ['Python', 'Django', 'JavaScript', 'React']
    }
    return render(request, 'resume.html', context)