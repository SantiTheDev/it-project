from .models import Users, Documents, Repositories
from .serializers import UsersSerializers ,DocumentsSerializers, RepositoriesSerializers
from rest_framework import viewsets, permissions

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    permission_classes = [permissions.AllowAny]

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializers
    permission_classes = [permissions.AllowAny]

class RepositoriesViewSet(viewsets.ModelViewSet):
    queryset = Repositories.objects.all()
    serializer_class = RepositoriesSerializers
    permission_classes = [permissions.AllowAny]
