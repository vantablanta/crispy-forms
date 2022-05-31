from django.shortcuts import render
from .forms import RandomForm
# Create your views here.
def home(request):
    forms = RandomForm()
    context = {'forms': forms}
    return render(request, 'formsapp/index.html', context)