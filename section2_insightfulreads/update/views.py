from django.shortcuts import render, redirect
from addnew.models import Article

# Create your views here.

article_entered = ''

def home(request):
    return render(request, 'update/update.html')

def details(request):
    article = request.GET.get('article', '').title()
    request.session['article_entered'] = article

    articles = list(Article.objects.values_list('article_name', flat=True))

    status = 'true'
    status = {'article' : article, 'status' : status}


    if article == '':
        status['status'] = 'empty'
        return render(request, 'update/update.html', status)

    elif article in articles:
        return render(request, 'update/details.html', status)
    
    else:
        status['status'] = 'false'
        return render(request, 'update/update.html', status)
    

def updated(request):
    article_entered = request.session.get('article_entered', '').title()
    name = request.GET.get('article', '').title()
    author = request.GET.get('author', '').title()
    date = request.GET.get('date', '')
    category = request.GET.get('category', '')

    all = 'true'
    parameters = {'article': article_entered, 'author' : author, 'date' : date, 'category' : category, 'all' : all}
    
    if author and date and category:
        a = Article.objects.get(article_name = article_entered)
        a.article_name = name
        a.author_name = author
        a.publishing_date = date
        a.category = category
        a.save()
        return redirect('http://127.0.0.1:8000/?purpose=updated&article='+article_entered)
    
    parameters['status'] = 'false'
    return render(request, 'update/details.html', parameters)