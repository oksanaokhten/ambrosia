from django.shortcuts import render
from .models import News


def all_news(request):
    """ A view to show all store news """

    news = News.objects.all()
    
    context = {
        'news': news,
    }

    return render(request, 'news/store_news.html', context)
