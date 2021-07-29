from django.db import models

CATEGORY = [
    ("Kitchen Appliances", "Kitchen Appliances"),
    ("Electronics and Accessories", "Electronics & Accessories"),
    ("Sports & Outdoors", "Sports & Outdoors"),
    ("Kids and Toys", "Kids and Toys"),
    ("Health & Beauty", "Health & Beauty"),
    ("Groceries & Foods", "Groceries and Foods"),
    ("Fashion", "Fashion"),
]

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=255)
    productImg = models.ImageField(upload_to='products', verbose_name="Product Image")
    price = models.IntegerField()
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    ratings = models.DecimalField(decimal_places=1, max_digits=3)
    category = models.CharField(max_length=100, choices=CATEGORY, unique=True, null=True)
    # vendor = models.C

    def __str__(self):
        return self.name
