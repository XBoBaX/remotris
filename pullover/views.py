from django.shortcuts import render
from .models import pullover


def main(request):
    list = pullover.objects.all().order_by('top')
    return render(request, 'main/index.html', {'page': '2', 'list': list})
