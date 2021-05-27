from django.db import models
from django.urls import reverse_lazy


class Categories(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    file = models.FileField(blank=True, upload_to='files/%Y/%m/%d', verbose_name='Файл')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
