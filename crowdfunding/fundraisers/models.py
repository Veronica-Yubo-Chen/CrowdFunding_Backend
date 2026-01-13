from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Fundraiser(models.Model):
    '''
    title - this field should contain short strings of characters
    description - this field should contain longer blocks of text
    goal - this field should contain an integer
    etc...
    '''
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_fundraisers'
    )
    
    

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        Fundraiser, 
        related_name='pledges', 
        on_delete=models.CASCADE)
    
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )