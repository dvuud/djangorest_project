from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to = 'product_images', verbose_name='Фото')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'    