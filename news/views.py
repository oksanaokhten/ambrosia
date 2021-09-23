from django.shortcuts import render, get_object_or_404
from .models import News


def all_news(request):
    """ A view to show all store news """

    news = News.objects.all()
    
    context = {
        'news': news,
    }

    return render(request, 'news/store_news.html', context)


def news_detail(request, news_id):
    """ A view to show individual store news details """

    store_news = get_object_or_404(News, pk=news_id)

    context = {
        'store_news': store_news,
    }

    return render(request, 'news/store_news_detail.html', context)
