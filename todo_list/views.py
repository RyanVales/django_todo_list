from django.shortcuts import render
from .models import List
from .forms import ListForm

def home(request):
    all_items = List.objects.all()  # Added parentheses to actually call the method
    context = {'all_items': all_items}
    return render(request, 'todo_list/home.html', context)  # Fixed template path

def about(request):
    context = {'myname': 'Bob'}
    return render(request, 'todo_list/about.html', context)  # Fixed template path