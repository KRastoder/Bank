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
