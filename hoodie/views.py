from django.shortcuts import render
from .models import hoodie


def main(request):
    list = hoodie.objects.all().order_by('top')
    return render(request, 'main/index.html', {'page': '3', 'list': list})
