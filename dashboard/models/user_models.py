from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Eğer kullanıcıya ekstra alan eklemek istersen
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Diğer alanları buraya ekleyebilirsin.

    def __str__(self):
        return self.username
