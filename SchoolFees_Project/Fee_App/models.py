from django.db import models

class Fee(models.Model):
    grade = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.grade} - {self.amount}"
