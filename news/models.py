from django.db import models

# Create your models here.


class NewsCategory(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class News(models.Model):
    news_head = models.CharField(max_length=50)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    main_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_head

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
