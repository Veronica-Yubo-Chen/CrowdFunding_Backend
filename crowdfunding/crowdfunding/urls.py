from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from users.views import CustomAuthToken


class ApiRoot(APIView):
    """Root API endpoint with available endpoints information"""
    def get(self, request):
        return Response({
            "message": "Welcome to Glwup API",
            "name": "Glwup - Beauty Product Crowdfunding Platform",
            "description": "A crowdfunding platform for beauty enthusiasts to fund product reviews and comparisons",
            "version": "1.0",
            "features": {
                "funding_protection": "Campaigns automatically close when goal is reached",
                "duplicate_pledge_prevention": "Users can only pledge once per campaign",
                "pledge_validation": "Pledges must be > $0 and campaign must accept pledges",
                "campaign_filtering": "Search, filter by category, funding status, and availability",
                "user_statistics": "Track total pledged and campaigns created",
            },
            "endpoints": {
                "authentication": {
                    "login": "POST /api-token-auth/",
                },
                "users": {
                    "list": "GET /users/",
                    "create": "POST /users/",
                    "current": "GET /users/me/ (requires authentication)",
                    "retrieve": "GET /users/<id>/",
                    "update": "PUT /users/<id>/ (requires authentication, owner only)",
                    "delete": "DELETE /users/<id>/ (requires authentication, owner only)",
                },
                "fundraisers": {
                    "list": "GET /fundraisers/ (supports query parameters)",
                    "list_parameters": {
                        "search": "Search by title or description (e.g., ?search=skincare)",
                        "category": "Filter by category (e.g., ?category=makeup)",
                        "is_open": "Filter by status open/closed (e.g., ?is_open=true)",
                        "funded": "Filter by funding status (e.g., ?funded=false)",
                    },
                    "create": "POST /fundraisers/ (requires authentication)",
                    "retrieve": "GET /fundraisers/<id>/",
                    "update": "PUT /fundraisers/<id>/ (requires authentication, owner only)",
                    "delete": "DELETE /fundraisers/<id>/ (requires authentication, owner only)",
                    "fields_returned": {
                        "total_pledged": "Calculated total amount pledged",
                        "is_funded": "Boolean - campaign reached goal",
                        "can_accept_pledges": "Boolean - campaign accepts new pledges",
                        "pledge_count": "Number of pledges (detail endpoint only)",
                        "deadline": "Optional campaign deadline",
                        "is_public": "Campaign visibility",
                    }
                },
                "pledges": {
                    "list": "GET /pledges/",
                    "create": "POST /pledges/ (requires authentication, validates against campaign limits)",
                    "retrieve": "GET /pledges/<id>/",
                    "update": "PUT /pledges/<id>/ (requires authentication, supporter only, validates campaign status)",
                    "delete": "DELETE /pledges/<id>/ (requires authentication, supporter only)",
                    "validation_rules": {
                        "amount_validation": "Pledge amount must be > 0",
                        "duplicate_prevention": "One pledge per user per campaign",
                        "campaign_status": "Campaign must accept pledges (not funded, open, deadline not passed)",
                    }
                }
            }
        })


def custom_404(request, exception):
    return JsonResponse({"detail": "Not found."}, status=404)


handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRoot.as_view(), name='api_root'),
    path('', include('fundraisers.urls')),
    path('', include('users.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
