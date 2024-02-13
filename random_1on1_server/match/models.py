from django.db import models

# Create your models here.
class UserMatch(models.Model):
    users = models.ManyToManyField('accounts.User', related_name='matches')

    is_active = models.BooleanField(default=True)

    start = models.DateField(help_text='usually start of week')
    end = models.DateField(help_text='usually end of week')

    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


