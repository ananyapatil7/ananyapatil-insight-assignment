from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def home(request):
    return render(request, 'addnew/add.html')

def added(request):
    article = request.GET.get('article', '').title()
    author = request.GET.get('author', '').title()
    date = request.GET.get('date', '')
    category = request.GET.get('category', '')

    status = 'true'
    status = {'status' : status}

    if article and author and date and category:
        new_article = Article(article_name = article, author_name = author, publishing_date = date, category = category)
        new_article.save()
        return redirect('http://127.0.0.1:8000/?purpose=added&article=' + article)
    
    else:
        status['status'] = 'false'
        return render(request, 'addnew/add.html', status)