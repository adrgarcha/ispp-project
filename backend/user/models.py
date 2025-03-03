from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.utils import timezone
from django.forms import ValidationError

class User(AbstractUser):
    birth_date = models.DateField()
    language = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(blank=False, default=True)
    image = models.ImageField(null=True, blank=False)
    points = models.PositiveIntegerField(null=False, default=0)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date']

    def clean(self):
        super().clean()
        if self.email.strip() == '':
            raise ValidationError("El email no puede estar vacio")
        if self.username.strip() == '':
            raise ValidationError("El usuario no puede estar vacio")
        if self.first_name.strip() == '':
            raise ValidationError("El nombre no puede estar vacio")
        if self.last_name.strip() == '':
            raise ValidationError("Los apellidos no pueden estar vacios")
        if self.birth_date == '':
            raise ValidationError("La fecha de nacimiento no puede estar vacia")
        if not isinstance(self.birth_date, datetime.date):
            birth_date = datetime.datetime.strptime(self.birth_date, "%Y-%m-%d").date()
        else:
            birth_date = self.birth_date
        if birth_date and birth_date > timezone.now().date():
            raise ValidationError("La fecha de nacimiento debe ser en el pasado.")
        sixteen_years_ago = timezone.now().date() - timezone.timedelta(days=16*365)
        if birth_date and birth_date > sixteen_years_ago:
            raise ValidationError("Debes tener al menos 16 años de edad.")
        eighty_years_ago = timezone.now().date() - timezone.timedelta(days=80*365)
        if birth_date and birth_date < eighty_years_ago:
            raise ValidationError("Debes tener menos de 80 años de edad.")

    def save(self, *args, **kwargs):
        self.clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username