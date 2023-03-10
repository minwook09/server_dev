# Generated by Django 4.1.7 on 2023-03-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_loginuser_user_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='age',
            field=models.IntegerField(default=20, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='birth_day',
            field=models.DateField(null=True, verbose_name='생년월일'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='email',
            field=models.CharField(default=False, max_length=256, verbose_name='이메일 주소'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='gender',
            field=models.CharField(default='male', max_length=6, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='name',
            field=models.CharField(default=False, max_length=20, verbose_name='이름'),
        ),
    ]
