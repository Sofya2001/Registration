
from django.shortcuts import render
def spisok(request):
    return render(request,'kinomir/spisok.html', locals())