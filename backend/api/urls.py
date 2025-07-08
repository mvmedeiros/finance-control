from django.urls import path
from .views import create_transaction, get_transactions, update_transaction, delete_transaction
from .views import create_category, get_categories, update_category, delete_category
from .views import create_user, get_users, update_user, delete_user
from .views import create_account, get_accounts, update_account, delete_account

urlpatterns = [
    path('transactions/', get_transactions, name='get_transactions'),
    path('transactions/create/', create_transaction, name='create_transaction'),
    path('transactions/update/<int:pk>', update_transaction, name='update_transaction'),
    path('transactions/delete/<int:pk>', delete_transaction, name='delete_transaction'),
    path('categories/', get_categories, name='get_categories'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/update/<int:pk>', update_category, name='update_category'),
    path('categories/delete/<int:pk>', delete_category, name='delete_category'),
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/update/<int:pk>', update_user, name='update_user'),
    path('users/delete/<int:pk>', delete_user, name='delete_user'),
    path('accounts/', get_accounts, name='get_accounts'),
    path('accounts/create/', create_account, name='create_account'),
    path('accounts/update/<int:pk>', update_account, name='update_account'),
    path('accounts/delete/<int:pk>', delete_account, name='delete_account'),
]