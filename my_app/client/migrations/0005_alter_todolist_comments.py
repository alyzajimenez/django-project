# Generated by Django 5.0.3 on 2024-03-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_comments_todolist_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='comments',
            field=models.ManyToManyField(blank=True, to='client.comment'),
        ),
    ]