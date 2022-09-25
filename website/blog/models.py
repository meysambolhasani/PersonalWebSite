from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    author_image = models.ImageField(
        upload_to="static/images/authors", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = models.ImageField(
        upload_to="blog/static/images/posts", null=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True, null=False)
    excerpt = models.CharField(max_length=250, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.slug


class Comment(models.Model):

    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
