from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Бөлүм'
        verbose_name_plural = 'Бөлүмдөр'


    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.IntegerField(verbose_name='Категория id')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)
    class Meta:
        verbose_name='Китеп'
        verbose_name_plural = 'Китептер'

    def __str__(self):
        return self.name