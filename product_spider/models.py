from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    price = models.CharField(max_length=200)
    image_url = models.URLField()

    class Meta:
        db_table = 'product_data'