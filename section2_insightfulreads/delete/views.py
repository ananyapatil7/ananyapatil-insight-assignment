from django.shortcuts import render, redirect
from addnew.models import Article

# Create your views here.

def home(request):
    return render(request, 'delete/delete.html')

def deleted(request):
    article = request.GET.get('article', 'default').title()
    
    articles = list(Article.objects.values_list('article_name', flat=True))
    
    status = 'true'
    status = {'article' : article, 'status' : status}

    if article == '':
        status['status'] = 'empty'
        return render(request, 'delete/delete.html', status)

    elif article in articles:
        a = Article.objects.get(article_name = article)
        a.delete()
    
        return redirect('http://127.0.0.1:8000/?purpose=deleted&article='+article)

    else:        
        status['status'] = 'false'
        return render(request, 'delete/delete.html', status)