from django.db import models

class kgfMovieTicket(models.Model):
    Name=models.CharField(max_length=50)
    Tickets=models.IntegerField(max_length=50)
class beastMovieTicket(models.Model):
    Name=models.CharField(max_length=50)
    Tickets=models.IntegerField(max_length=50)
class rrrMovieTicket(models.Model):
    Name=models.CharField(max_length=50)
    Tickets=models.IntegerField(max_length=50)
