from django.shortcuts import render,redirect
from .models import News,News_Letter
from django.db.models import Q
from .forms import NewsForm
# Create your views here.
def news_letter_view(request,id):
    news_letter = News_Letter.objects.get(pk=id)
    news_list = news_letter.news.all()
    news_letter_list = News_Letter.objects.all()
    form = NewsForm(request.POST or None)
    if form.is_valid():
        new_news = form.save(commit=False)
        new_news.author = request.user.alumni
        new_news.save()
        form.save_m2m()
        return redirect(request.get_full_path())
    context = {
        'news_list':news_list,
        'forms':form,
        'news_letter_list':news_letter_list,
        'news_letter':news_letter,
    }
    print('yoo')
    return render(request,"news/news_view.html",context)


def news_details(request,id):
    news = News.objects.get(pk=id)
    context = {
        'news':news,
    }
    return render(request,"news/news_details.html",context)


def news_search_result(request):
    value = request.POST['search_news']
    query = News.objects.filter(headline__icontains=value)
    print(query)
    context = {
        'news_list':query,
    }
    return render(request,"news/news_search_result.html",context)
