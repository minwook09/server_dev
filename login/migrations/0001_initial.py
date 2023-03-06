# Generated by Django 4.1.7 on 2023-03-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=False, max_length=20)),
                ('user_pw', models.CharField(default=False, max_length=20)),
            ],
            options={
                'verbose_name': 'login test table',
                'db_table': 'login_user',
            },
        ),
    ]
