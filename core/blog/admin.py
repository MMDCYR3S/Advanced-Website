from django.contrib import admin
from blog.models import Category, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_date",
        "published_date",
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
