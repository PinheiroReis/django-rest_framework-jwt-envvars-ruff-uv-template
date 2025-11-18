from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    categories = models.ManyToManyField(Category, related_name="items")
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Item-{self.id}"
