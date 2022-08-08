from django.shortcuts import render, redirect
from .forms import PostForm

def home(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        form = PostForm()

    context = {
        'forms':form
    }

    return render(request, 'blog/base.html', context)
