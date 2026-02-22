from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from django.db.models import Q
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Only the owner can edit/delete; others can only read."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSupporterOrReadOnly(permissions.BasePermission):
    """Only the pledge supporter can edit/delete; others can only read."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user


class FundraiserList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        # Get base fundraisers
        fundraisers = Fundraiser.objects.all()
        
        # Filter by search query
        search_query = request.query_params.get('search', '')
        if search_query:
            fundraisers = fundraisers.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Filter by category
        category = request.query_params.get('category', '')
        if category:
            fundraisers = fundraisers.filter(category__icontains=category)
        
        # Filter by status (open/closed)
        is_open = request.query_params.get('is_open', '')
        if is_open.lower() == 'true':
            fundraisers = fundraisers.filter(is_open=True)
        elif is_open.lower() == 'false':
            fundraisers = fundraisers.filter(is_open=False)
        
        # Filter by funding status
        funded = request.query_params.get('funded', '')
        if funded.lower() == 'true':
            # Return only funded campaigns
            fundraisers = [f for f in fundraisers if f.is_funded()]
        elif funded.lower() == 'false':
            # Return only unfunded campaigns
            fundraisers = [f for f in fundraisers if not f.is_funded()]
        
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FundraiserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Fundraiser.objects.get(pk=pk)
        except Fundraiser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)

    def put(self, request, pk):
        fundraiser = self.get_object(pk)
        self.check_object_permissions(request, fundraiser)
        serializer = FundraiserDetailSerializer(fundraiser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fundraiser = self.get_object(pk)
        self.check_object_permissions(request, fundraiser)
        fundraiser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Set supporter from authenticated user
                pledge = Pledge(**serializer.validated_data, supporter=request.user)
                pledge.full_clean()  # Runs the clean() method
                pledge.save()
                return Response(PledgeSerializer(pledge).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {'detail': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    def get_object(self, pk):
        try:
            return Pledge.objects.get(pk=pk)
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        self.check_object_permissions(request, pledge)
        serializer = PledgeSerializer(pledge, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                pledge.full_clean()
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                return Response(
                    {'detail': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pledge = self.get_object(pk)
        self.check_object_permissions(request, pledge)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)