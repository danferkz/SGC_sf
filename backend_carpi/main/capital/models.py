# capital/models.py
from django.db import models

class Capital(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'capital'
        verbose_name = 'Capital'
        verbose_name_plural = 'Capital'

    def __str__(self):
        return f'Capital: {self.amount} on {self.date}'
