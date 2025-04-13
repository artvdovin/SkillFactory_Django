from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache

# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField (default=0)

    def update_rating(self):
        rt = 0
        for el in self.post_set.all():
            rt +=el.rating
        rt = rt*3
        for el in self.author.comment_set.all():
            rt = rt + el.rating
        for el in Comment.objects.filter(commentPost__author=self):
            rt = rt + el.rating
        self.rating=rt
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User,blank=True, null= True, related_name='categories')

    def __str__(self):
        return self.category

class Post (models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_TYPE = (
        (NEWS , "Новость"),
        (ARTICLE, "Статья")
    )


    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_add = models.DateTimeField (auto_now_add=True)
    title = models.CharField(max_length=255)
    post = models.TextField()
    rating = models.IntegerField(default=0)
    postCategory = models.ManyToManyField(Category, through="PostCategory") 
    categoryType = models.CharField(max_length=2, choices=CATEGORY_TYPE, default=NEWS)


    def like(self):
        self.rating+=1
        self.save()

    def dislike(self):
        self.rating-=1
        self.save()  

    def preview(self):
           return f"{self.post[:124]}..." 
    
    def get_absolute_url(self):
        return reverse('new', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его

class PostCategory (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment (models.Model):
    commentPost = models.ForeignKey (Post,on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    commentDate = models.DateTimeField (auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating+=1
        self.save()

    def dislike(self):
        self.rating-=1
        self.save()