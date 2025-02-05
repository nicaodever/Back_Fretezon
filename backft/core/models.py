from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id_user'
    )
    password = models.CharField(
        db_column='password',
        null=False,
        max_length=64
    )
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=255
    )
    email = models.EmailField(
        db_column='email',
        unique=True,
        null=False
    )
    phone = models.CharField(
        db_column='phone',
        null=False,
        max_length=25
    )
class Frete(models.Model):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id_post'
    )
    tp_veiculo = models.CharField(
        db_column='tp_veiculo',
        null=False,
        max_length=255
    )
    local_partida = models.CharField(
        db_column='local_partida',
        null=False,
        max_length=255
    )


