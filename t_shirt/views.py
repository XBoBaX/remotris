from django.shortcuts import render
from .models import t_shirt

def main(request):
    list = t_shirt.objects.all().order_by('top')
    return render(request, 'main/index.html', {'page': '1', 'list': list})
