from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ArticleView(View):
    articles = Article.published.get_queryset().order_by('-id')
    paginator = Paginator(articles, 3)
    template_name = 'blog/articles.html'
    context = {'articles': articles}

    def get(self, request):
        page = request.GET.get('page', 1)
        try:
            articles = self.paginator.page(page)
        except PageNotAnInteger:
            articles = self.paginator.page(1)
        except EmptyPage:
            articles = self.paginator.page(self.paginator.num_pages)
        self.context['articles'] = articles
        return render(request, self.template_name, self.context)

    # def post(self, request):
    #     # page = request.GET.get('page', 3)
    #     # try:
    #     #     articles = self.paginator.page(page)
    #     # except PageNotAnInteger:
    #     #     articles = self.paginator.page(1)
    #     # except EmptyPage:
    #     #     articles = self.paginator.page(self.paginator.num_pages)
    #     # self.context['articles'] = articles
    #     return render(request, self.template_name, self.context)


class ArticleDetailView(View):
    template_name = 'blog/article_detail.html'

    def get(self, request, pk, slug):
        # article = Article.published.get(pk=pk, slug=slug)
        article = get_object_or_404(Article, pk=pk, slug=slug)
        context = {'article': article}
        return render(request, self.template_name, context)

    # def post(self, request, pk, slug):
    #     article = Article.published.get(pk=pk, slug=slug)
    #     context = {'article': article}
    #     return render(request, self.template_name, context)


class TestView(View):
    template_name = 'blog/test.html'

    def get(self, request):
        return render(request, self.template_name)
