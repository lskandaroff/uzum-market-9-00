

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Tavsif")

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Narxi"
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Chegirmadagi narxi"
    )

    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True
    )

    stock = models.PositiveIntegerField(default=0, verbose_name="Ombordagi soni")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ["-created_at"]
