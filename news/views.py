from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import News
from .forms import NewsForm


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


def add_news(request):
    """ Add a news to the store """
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added news!')
            return redirect(reverse('add_news'))
        else:
            messages.error(request, 'Failed to add news. Please ensure the form is valid.')
    else:
        form = NewsForm()
    template = 'news/add_news.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_news(request, news_id):
    """ Edit a news in the news manager """
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated store news!')
            return redirect(reverse('news_detail', args=[news.id]))
        else:
            messages.error(request, 'Failed to update store news. Please ensure the form is valid.')
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are editing {news.name}')

    template = 'news/edit_news.html'
    context = {
        'form': form,
        'news': news,
    }

    return render(request, template, context)
