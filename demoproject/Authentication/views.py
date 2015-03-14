from django.contrib.admin.utils import lookup_field

from Authentication.models import Account
from Authentication.serializers import AccountSerializer
from Authentication.permissions import IsAccountOwner
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        
        return (permissions.IsAuthenticated(), IsAccountOwner(),)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print serializer
        
        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
        return Response({
                         'status' : 'Bad Request',
                         'message' : 'Account could not be created with received data.'},
                        status=status.HTTP_400_BAD_REQUEST)
        