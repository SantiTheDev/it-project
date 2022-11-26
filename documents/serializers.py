from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, IntegerField, CharField
from .models import Users, Documents, Repositories


# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    rep_id= IntegerField()
    name = CharField()
    class Meta:
        fields = ('file_uploaded', 'rep_id', 'name')


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'date_joined')
        read_only_fields = ('date_joined',)


class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('name', 'data', 'rep_id','added_at')
        read_only_fields = ('added_at',)

class RepositoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Repositories
        fields = ('name','created_at', 'owner')
        read_only_fields = ('created_at',)
