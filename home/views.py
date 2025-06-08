from django.shortcuts import get_object_or_404, render
from .models import teachers

def index(request):
    teach = teachers.objects.all()
    return render(request, 'home/home.html', {'teach': teach})


def info(request, slug):
    teacher = get_object_or_404(teachers, slug=slug)
    return render(request, 'info/info.html', {'teacher': teacher})