from django.urls import path
# Импортируем созданное нами представление
from .views import News,NewsDetail, Search, NewsCreate, NewsEdit,NewsDel, ArticleCreate, ArticleEdit, ArticleDel,upgrade_me, CategoryListNew, subscribe


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', News.as_view(),name='news'), 
   path('<int:pk>', NewsDetail.as_view(), name="new"),
   path('search/', Search.as_view(), name='search'),
   path('news/create', NewsCreate.as_view(), name="new_create"),
   path ('news/<int:pk>/edit',NewsEdit.as_view(),name = "new_edit"),
   path ('news/<int:pk>/del',NewsDel.as_view(),name = "new_del"),
   path('article/create', ArticleCreate.as_view(), name="ar_create"),
   path ('article/<int:pk>/edit',ArticleEdit.as_view(),name = "ar_edit"),
   path ('article/<int:pk>/del',ArticleDel.as_view(),name = "ar_del"),
   path('upgrade/', upgrade_me, name = 'upgrade'),
   path('categories/<int:pk>', CategoryListNew.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   



]
