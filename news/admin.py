from django.contrib import admin
from news.models import NewsCategory, News

# Register your models here.


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['category_name', 'id']
    ordering = ['id']


admin.site.register(News)
