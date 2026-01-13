from django.db import models
from django.contrib.auth import get_user_model


class Fundraiser(models.Model):
    '''
    A beauty product comparison fundraiser.
    Users can create campaigns to crowdfund product reviews and comparisons.
    '''
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()  # Target amount to raise
    image = models.URLField()  # Product/campaign image URL
    is_open = models.BooleanField(default=True)  # Accepting supporters?
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_fundraisers'
    )
    # Beauty-specific fields for product comparison
    category = models.CharField(max_length=100, blank=True, default='')  # e.g., "Skincare", "Makeup"
    product_link = models.URLField(blank=True, default='')  # External link to buy the product

    def __str__(self):
        return self.title


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        Fundraiser,
        related_name='pledges',
        on_delete=models.CASCADE
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

    def __str__(self):
        return f"${self.amount} pledge to {self.fundraiser.title}"