from django.core.exceptions import ValidationError
from django.db import models

MAX_LENGTH = 63


class Musician(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    instrument = models.CharField(max_length=MAX_LENGTH)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def clean(self):
        if self.age < 14:
            raise ValidationError("Musicians must be at least 14 years old.")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
