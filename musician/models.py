from django.core.validators import MinValueValidator
from django.db import models

MAX_LENGTH = 63


class Musician(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    instrument = models.CharField(max_length=MAX_LENGTH)
    age = models.IntegerField(validators=[MinValueValidator(14)])
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
