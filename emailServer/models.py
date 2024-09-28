from django.db import models


class Email(models.Model):
    listEmail:models.CharField =models.CharField(max_length=100)
    def __str__(self):
        return self.listEmail

