from django.db import models


# Create your models here.
# 인원
class Person(models.Model):
    name = models.CharField(max_length=3)
    position = models.IntegerField()
    pot = models.IntegerField()
    team = models.IntegerField(default='5')
    odr = models.IntegerField(null=True)

# 직급
class Position(models.Model):
    position = models.CharField(max_length=4)

# 팀
class Team(models.Model):
    Team_name = models.TextField()

# pots
class Pots(models.Model):
    pot_name = models.CharField(max_length=3)
