from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name="Имя категории"
    )
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "title",
        ]


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        blank=True,
        verbose_name="Фото",
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name="В наличии",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name="Количество",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категория",
    )

    def my_func(self):
        return "Наши товары"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = [
            "-created_at",
        ]
