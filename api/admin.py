from django.contrib import admin
from . models import Article

# Register your models here.
class ArticleModel(admin.ModelAdmin):
    list_display = ['title', 'author', 'email', 'date']

admin.site.register(Article, ArticleModel)


