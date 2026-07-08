from django.db import models


class FoodCategory(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="foods")

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    price = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title