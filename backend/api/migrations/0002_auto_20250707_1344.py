# Generated by Django 5.2.3 on 2025-07-07 11:44

from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('api', 'Category')
    default_categories = [
        {'name': 'Salary', 'type': 'income'},
        {'name': 'Investment', 'type': 'income'},   
        {'name': 'Other', 'type': 'income'},
        {'name': 'House', 'type': 'expense'},
        {'name': 'Groceries', 'type': 'expense'},
        {'name': 'Hobby', 'type': 'expense'},
        {'name': 'Clothing', 'type': 'expense'},
        {'name': 'Other', 'type': 'expense'},
    ]

    for category in default_categories:
        Category.objects.get_or_create(**category)

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
