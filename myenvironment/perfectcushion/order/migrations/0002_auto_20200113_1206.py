# Generated by Django 3.0.2 on 2020-01-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='emailAddress',
        ),
    ]
