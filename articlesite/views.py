from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articlesite/form.html', {'form': form})

def article_detail(request, pk):
    article = Article.objects.last()
    return render(request, 'articlesite/article.html', {'article': article})

def index(request):
    articles = Article.objects.all()
    return render(request, 'articlesite/index.html', {'articles': articles})
