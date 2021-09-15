from .models import Link
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST" and request.POST.get('name') and request.POST.get('long_link'):
        name = request.POST.get('name')
        long_link = request.POST.get('long_link')
        link = Link(name=name, long_link=long_link)
        link.save()
    links = Link.objects.all().order_by('-id')
    return render(request, 'index.html', {'links': links})


def get_link(request, pk):
    try:
        link = Link.objects.get(pk=pk)
        return redirect(link.long_link)
    except:
        return HttpResponse('invaild link')
