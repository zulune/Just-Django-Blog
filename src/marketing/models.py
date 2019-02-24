from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField(_("Email"), max_length=254)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return self.email