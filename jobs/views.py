from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    print(jobs)
    return render(request, 'jobs/home.html', {'jobs':jobs})

def view(request, pk):
    view = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/view.html', {'view':view, 'pk':pk})