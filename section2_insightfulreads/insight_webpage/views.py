from django.shortcuts import render, redirect
from addnew.models import Article

def home(request):
    articles = list(Article.objects.all())
    purpose = request.GET.get('purpose', '')
    article = request.GET.get('article', '')
    n = len(articles)
    parameters = {'purpose' : purpose, 'article' : article, 'articles' : articles, 'range' : range(n)}
    return render (request, 'home.html', parameters)

def article(request):
    article = request.GET.get('article', '')
    a = Article.objects.get(article_name = article)
    article_details = {'name' : a.article_name, 'author' : a.author_name, 'date' : a.publishing_date, 'category' : a.category}
    return render(request, 'article.html', article_details)

def search(request):
    search = request.GET.get('search', '').title()
    articles = list(Article.objects.values_list('article_name', flat=True))
    authors = list(Article.objects.values_list('author_name', flat=True))
    categories = list(Article.objects.values_list('category', flat=True))
    
    if search in ['', ' ']:
        return redirect('http://127.0.0.1:8000')

    elif search in articles:
        a = Article.objects.get(article_name = search)
        article_details = {'name' : a.article_name, 'author' : a.author_name, 'date' : a.publishing_date, 'category' : a.category, 
                           'status' : 'article', 'purpose' : 'searched'}
        return render(request, 'search.html', article_details)
            
    elif search in authors:
        articles_list = list(Article.objects.filter(author_name = search))
        n=len(articles_list)
        parameters={'purpose' : 'searched', 'articles' : articles_list, 'range' : range(n), 'search' : search, 'n' : n}
        return render(request, 'home.html', parameters)
    
    elif search in categories:
        articles_list = list(Article.objects.filter(category = search))
        n=len(articles_list)
        parameters={'purpose' : 'searched', 'articles' : articles_list, 'range' : range(n), 'search' : search, 'n' : n}
        return render(request, 'home.html', parameters)
    
    else:
        status = {'status' : 'not_found', 'search' : search}
        return render(request, 'search.html', status)