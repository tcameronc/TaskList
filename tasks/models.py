from django.db import models

import tasks.apps


# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task


# not null constraint error appears if blank=True & null=True fails