# Generated by Django 4.1.7 on 2023-03-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_id',
            field=models.CharField(default=False, max_length=20, unique=True),
        ),
    ]