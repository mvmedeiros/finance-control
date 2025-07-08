from rest_framework import serializers
from .models import Transaction, Category, User, Account

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    class Meta:
        model = Transaction
        fields = '__all__'  # Include all fields from the Transaction model

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Account model.
    """
    class Meta:
        model = Account
        fields = '__all__'