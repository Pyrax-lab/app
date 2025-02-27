from django.db import models
from django.contrib.auth.models import User 


# Create your models her
# e.


class User(User):
    email = models.EmailField(verbose_name="email")
