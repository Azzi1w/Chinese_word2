# Generated by Django 5.1.2 on 2024-11-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_word', '0005_alter_words_date_str'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words',
            name='date_dj',
        ),
    ]
