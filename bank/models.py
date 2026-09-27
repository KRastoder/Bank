from django.db import models

# models

# User:
# 	UUID PK id
# 	CHARFIELD email
# 	CHARFIELD password  OVO DA HASHUJEMO

# NOVI KORISNIK
# Svaki put kad napravimo korsinka ID =ID+1


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Account')
    balance = models.FloatField()
    pin = models.IntegerField(max_length=9999)
    