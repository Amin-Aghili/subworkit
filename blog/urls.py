from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='articles'),
    path('<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('test/', views.TestView.as_view(), name='test'),
]
