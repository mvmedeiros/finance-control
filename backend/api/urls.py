from django.urls import path
from .views import get_transactions, create_transaction, delete_transaction, update_transaction

urlpatterns = [
    path('transactions/', get_transactions, name='get_transactions'),
    path('transactions/create/', create_transaction, name='create_transaction'),
    path('transactions/update/<int:pk>', update_transaction, name='update_transaction'),
    path('transactions/delete/<int:pk>', delete_transaction, name='delete_transaction'),
]
