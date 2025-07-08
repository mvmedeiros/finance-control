from django.db import models

# Create your models here.
class Transaction(models.Model):
    """
    Model to represent a financial transaction.
    """
    TRANSACTION_TYPES = [
        ('income', 'income'),
        ('expense', 'expense'),
        ('transfer', 'transfer'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=TRANSACTION_TYPES)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey to Category model
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # ForeignKey to User model
    account = models.CharField(max_length=255) # Assuming account is a string, could be a ForeignKey to an Account model

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount} - {self.category}"

class Category(models.Model):
    """
    Model to represent a category for transactions.
    """
    TRANSACTION_TYPES = [
        ('income', 'income'),
        ('expense', 'expense'),
        ('transfer', 'transfer'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(choices=TRANSACTION_TYPES)

    class Meta:
        unique_together = ['name', 'type']  # optional: unique within type

    def clean(self):
        self.name = self.name.strip().title() # Ensure name is stripped of whitespace and title-cased
        self.type = self.type.strip().lower()  # Ensure type is stripped of whitespace and lower-cased

        # Check for existing category with the same name and type
        if Category.objects.filter(name=self.name, type=self.type).exists():
            raise ValueError(f"Category with name '{self.name}' and type '{self.type}' already exists.")
        
    def save(self, *args, **kwargs):
        self.full_clean() # Call clean method to validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.type})"

class User(models.Model):
    """
    Model to represent a user.
    """
    username = models.CharField(max_length=255, unique=True)
    # Authentication strategy will be implemented later, for now just a username for filtering purposes

    def __str__(self):
        return self.username