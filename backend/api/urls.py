from django.urls import path
from .views import get_transactions, create_transaction, delete_transaction, update_transaction, get_categories, create_category, update_category, delete_category

urlpatterns = [
    path('transactions/', get_transactions, name='get_transactions'),
    path('transactions/create/', create_transaction, name='create_transaction'),
    path('transactions/update/<int:pk>', update_transaction, name='update_transaction'),
    path('transactions/delete/<int:pk>', delete_transaction, name='delete_transaction'),
    path('categories/', get_categories, name='get_categories'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/update/<int:pk>', update_category, name='update_category'),
    path('categories/delete/<int:pk>', delete_category, name='delete_category'),
]
