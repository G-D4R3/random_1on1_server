from django.db import models

# Create your models here.
class UserMatch(models.Model):
    users = models.ManyToManyField('accounts.User', related_name='matches')

    is_active = models.BooleanField(default=True)

    start = models.DateField(help_text='usually monday')
    end = models.DateField(help_text='usually friday')

    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


