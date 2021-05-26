from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
