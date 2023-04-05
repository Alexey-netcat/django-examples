from django.shortcuts import render, redirect  
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, "news/news_home.html", {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'from': form,
        'error': error
    }

    return render(request, 'news/create.html', data)