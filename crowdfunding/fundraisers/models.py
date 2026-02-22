from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone


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
    deadline = models.DateTimeField(null=True, blank=True)  # Optional campaign deadline
    is_public = models.BooleanField(default=True)  # Public or private campaign
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

    def get_total_pledged(self):
        """Calculate total amount pledged to this fundraiser"""
        pledges = self.pledges.all()
        return sum(pledge.amount for pledge in pledges)

    def is_funded(self):
        """Check if campaign has reached its funding goal"""
        return self.get_total_pledged() >= self.goal

    def can_accept_pledges(self):
        """Check if campaign is still accepting pledges"""
        # Campaign must be open, goal not reached, and (if deadline set) not expired
        if not self.is_open or self.is_funded():
            return False
        if self.deadline and timezone.now() > self.deadline:
            return False
        return True


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
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

    class Meta:
        unique_together = ('fundraiser', 'supporter')  # Prevent duplicate pledges

    def __str__(self):
        return f"${self.amount} pledge to {self.fundraiser.title}"

    def clean(self):
        """Validate pledge before saving"""
        # Validate amount
        if self.amount <= 0:
            raise ValidationError("Pledge amount must be greater than zero.")
        
        # Check if campaign accepts pledges
        if not self.fundraiser.can_accept_pledges():
            raise ValidationError("This campaign is no longer accepting pledges.")
        
        # Check for duplicate pledges from same user
        existing_pledge = Pledge.objects.filter(
            fundraiser=self.fundraiser,
            supporter=self.supporter
        ).exclude(pk=self.pk)  # Exclude current instance when updating
        if existing_pledge.exists():
            raise ValidationError("You have already pledged to this campaign.")