from django.db import models

# Create your models here.
class Transaction(models.Model):
    """
    Model to represent a financial transaction.
    """
    INCOME = 'Income'
    EXPENSE = 'Expense'
    TRANSFER = 'Transfer'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
        (TRANSFER, 'Transfer'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=TYPE_CHOICES)
    category = models.CharField(max_length=255)
    user = models.CharField(max_length=255) # Assuming user is a string, could be a ForeignKey to a User model
    account = models.CharField(max_length=255) # Assuming account is a string, could be a ForeignKey to an Account model

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount} - {self.category}"

class Category(models.Model):
    """
    Model to represent a category for transactions.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name