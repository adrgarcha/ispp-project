from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    birth_date = models.DateField()
    language = models.CharField(max_length=50, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date']

    def clean(self):
        super().clean()
        if self.birth_date and self.birth_date > timezone.now().date():
            raise ValidationError("La fecha de nacimiento debe ser en el pasado.")
        sixteen_years_ago = timezone.now().date() - timezone.timedelta(days=16*365)
        if self.birth_date and self.birth_date > sixteen_years_ago:
            raise ValidationError("Debes tener al menos 16 años de edad.")
        eighty_years_ago = timezone.now().date() - timezone.timedelta(days=80*365)
        if self.birth_date and self.birth_date < eighty_years_ago:
            raise ValidationError("Debes tener menos de 80 años de edad.")

    def __str__(self):
        return self.username
