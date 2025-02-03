from django.db import models
from django.contrib.auth.models import User

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