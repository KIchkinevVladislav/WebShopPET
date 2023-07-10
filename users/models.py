from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to='users_images', 
        null=True, 
        blank=True
        )
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)


class EmailVerifivation(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f'EmailVerifivation object for {self.user.email}'