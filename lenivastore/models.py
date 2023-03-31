import os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
# from django.template.defaultfilters import slugify

MAX_AMOUNT_STARS = 5
MIN_AMOUNT_STARS = 0
VALIDATOR_MESSAGE = f'Рейтинг/кол-во звезд от {MIN_AMOUNT_STARS} до {MAX_AMOUNT_STARS}'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)  # db_index=True
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lenivastore:product_list_by_category', args=[self.slug])


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, related_name='subcategories',
        verbose_name="Категория",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return os.path.join('images/', filename)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products',
        verbose_name="Категория",
        on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name='products',
        verbose_name="Подкатегория", null=True,
        on_delete=models.SET_NULL, default=1
    )
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True, verbose_name="Описание")  # Empty value
    features = models.TextField(blank=True, verbose_name="Характеристики")  # Empty value
    price = models.PositiveIntegerField(verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    stock = models.PositiveIntegerField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    image = models.ImageField(upload_to=get_upload_path, blank=True,
                              verbose_name="Изображение товара")
    rating = models.DecimalField(
        blank=True, null=True, verbose_name="Рейтинг", max_digits=2, decimal_places=1,
        validators=(MaxValueValidator(MAX_AMOUNT_STARS, VALIDATOR_MESSAGE),
                    MinValueValidator(MIN_AMOUNT_STARS, VALIDATOR_MESSAGE)))
    stars = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name="Кол-во звезд",
        validators=(MaxValueValidator(MAX_AMOUNT_STARS, VALIDATOR_MESSAGE),))
    is_popular = models.BooleanField(default=False, verbose_name="Популярный")

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lenivastore:product_detail', args=[self.id, self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.brand_name)
    #     super(Brand, self).save(*args, **kwargs)


class News (models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    link = models.CharField(max_length=300, unique=True, blank=True, verbose_name="Ссылка")  # db_index=True
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение_новости")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
