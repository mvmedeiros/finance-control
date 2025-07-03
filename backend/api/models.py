from django.db import models

# Create your models here.
class Transaction(models.Model):
    """
    Model to represent a financial transaction.
    """
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSFER = 'TR'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
        (TRANSFER, 'Transfer'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount} - {self.category}"