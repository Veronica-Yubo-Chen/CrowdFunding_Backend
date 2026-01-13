from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from users.views import CustomAuthToken


def custom_404(request, exception):
    return JsonResponse({"detail": "Not found."}, status=404)


handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fundraisers.urls')),
    path('', include('users.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
