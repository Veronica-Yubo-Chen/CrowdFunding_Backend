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
                    "list": "GET /fundraisers/",
                    "create": "POST /fundraisers/ (requires authentication)",
                    "retrieve": "GET /fundraisers/<id>/",
                    "update": "PUT /fundraisers/<id>/ (requires authentication, owner only)",
                    "delete": "DELETE /fundraisers/<id>/ (requires authentication, owner only)",
                },
                "pledges": {
                    "list": "GET /pledges/",
                    "create": "POST /pledges/ (requires authentication)",
                    "retrieve": "GET /pledges/<id>/",
                    "update": "PUT /pledges/<id>/ (requires authentication, supporter only)",
                    "delete": "DELETE /pledges/<id>/ (requires authentication, supporter only)",
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
