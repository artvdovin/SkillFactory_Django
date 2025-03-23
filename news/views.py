from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post, Category
from .filters import PostFilter
from .form import NewsForm
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
from django.views import View


# Create your views here.





class News(ListView):
    model = Post
    ordering = '-date_add'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

class NewsDetail (DetailView):
    model=Post
    template_name = 'new.html'
    context_object_name = 'new'

class Search (ListView):
    model = Post
    ordering = '-date_add'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsCreate (CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_post')
    model = Post
    form_class = NewsForm
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)
    

class NewsEdit (LoginRequiredMixin,UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post')
    model = Post
    form_class = NewsForm
    template_name = 'news_create.html'
    


class NewsDel (DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy ('news')    

class ArticleCreate (CreateView):
    model = Post
    form_class = NewsForm
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)
    
class ArticleEdit (UpdateView):
    model = Post
    form_class = NewsForm
    template_name = 'article_create.html'
class ArticleDel (DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy ('news') 

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/new/')


class CategoryListNew(News):
    model = Post
    template_name = 'category_list.html'
    context_object_name = "category_news_list"

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory = self.category).order_by('-date_add')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['is_not_subscribe'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context
    

@login_required
def subscribe(request,pk):
    user = request.user
    category = Category.objects.get(id=pk) 
    category.subscribers.add(user)

    messange = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category':category,'messange':messange})       

        