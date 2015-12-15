from django.db import models

class Contestant(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	amount_of_tickets = models.IntegerField(default=0)
	

class Lottery(models.Model):
	name = models.CharField(max_length=30)
	amount_of_contestants = models.IntegerField(default=0)
	total_amount_of_tickets = models.IntegerField(default=0)
	winner = models.ForeignKey(Contestant, null = True, on_delete=models.CASCADE)
	lot_date = models.DateTimeField('drawing date', null = True, default='2015-12-15')