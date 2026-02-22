from rest_framework import serializers
from django.apps import apps
from django.core.exceptions import ValidationError as DjangoValidationError

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers', 'Pledge')
        fields = ['id', 'amount', 'comment', 'anonymous', 'fundraiser', 'supporter', 'date_created']
        read_only_fields = ['date_created']

    def validate_amount(self, value):
        """Validate pledge amount is positive"""
        if value <= 0:
            raise serializers.ValidationError("Pledge amount must be greater than zero.")
        return value

    def validate(self, data):
        """Validate pledge against campaign constraints"""
        fundraiser = data.get('fundraiser')
        supporter = data.get('supporter')
        
        # Check if campaign accepts pledges
        if not fundraiser.can_accept_pledges():
            raise serializers.ValidationError(
                "This campaign is no longer accepting pledges. Goal reached or campaign closed."
            )
        
        # Check for duplicate pledges
        existing_pledge = apps.get_model('fundraisers', 'Pledge').objects.filter(
            fundraiser=fundraiser,
            supporter=supporter
        ).exclude(pk=self.instance.pk if self.instance else None)
        
        if existing_pledge.exists():
            raise serializers.ValidationError(
                "You have already pledged to this campaign."
            )
        
        return data


class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_pledged = serializers.SerializerMethodField()
    is_funded = serializers.SerializerMethodField()
    can_accept_pledges = serializers.SerializerMethodField()
    
    class Meta:
        model = apps.get_model('fundraisers', 'Fundraiser')
        fields = [
            'id', 'title', 'description', 'goal', 'image', 'is_open', 
            'date_created', 'deadline', 'is_public', 'owner', 'category', 
            'product_link', 'total_pledged', 'is_funded', 'can_accept_pledges'
        ]
    
    def get_total_pledged(self, obj):
        """Calculate total pledged amount"""
        return obj.get_total_pledged()
    
    def get_is_funded(self, obj):
        """Check if campaign is funded"""
        return obj.is_funded()
    
    def get_can_accept_pledges(self, obj):
        """Check if campaign can still accept pledges"""
        return obj.can_accept_pledges()
    
class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    pledge_count = serializers.SerializerMethodField()
    
    class Meta(FundraiserSerializer.Meta):
        fields = FundraiserSerializer.Meta.fields + ['pledges', 'pledge_count']
    
    def get_pledge_count(self, obj):
        """Get count of pledges"""
        return obj.pledges.count()
        
class PledgeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers', 'Pledge')
        fields = '__all__'
        