from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    def __str__(self):
        return self.username