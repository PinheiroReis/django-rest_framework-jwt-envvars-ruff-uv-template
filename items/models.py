from django.db import models


class Item(models.Model):
    categories = models.ManyToManyField("categories.Category", related_name="items")
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item-{self.id}"
