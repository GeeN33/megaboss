# Generated by Django 4.2.1 on 2023-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megaboss_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]