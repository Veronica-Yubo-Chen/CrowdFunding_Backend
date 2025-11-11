from django.db import models

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
