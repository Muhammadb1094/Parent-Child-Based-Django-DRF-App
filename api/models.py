from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

