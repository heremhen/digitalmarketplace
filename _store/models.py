from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title

    def deduct_stock(self, quantity):
        if self.stock is not None:
            if quantity > 0:
                self.stock -= quantity
                self.save()

    def get_absolute_url(self):
        return reverse("product-info", args=[self.category.slug, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")
