from django.db import models
from encrypted_fields import fields


class LoginUser(models.Model):
    user_id = models.CharField(max_length=20, null=False, default=False, unique=True)
    user_pw = models.CharField(max_length=256, null=False, default=False)

    class Meta:
        db_table = 'login_user'
        verbose_name = 'login test table'
