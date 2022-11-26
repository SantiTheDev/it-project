from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from .models import Documents, Repositories
from datetime import datetime
import json

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        #lee la peticion en busca de un archivo y lo guardaen memoria
        file_uploaded = request.FILES.get('file_uploaded') 
        rep_id = request.POST.get('rep_id')
        name = request.POST.get('name')
        content_type = file_uploaded.content_type  
        response = "POST API and you have uploaded a {} file".format(content_type)
        now = datetime.now()
        # importante filtrar el repositorio donde fue creado el archivo
        rep = Repositories.objects.filter(id = rep_id) 

        #creas el nuevo dato

        file = Documents.objects.create(
            name = name,
            data = file_uploaded.read(),
            # este campo es una llave foreanea solo acepta instancias de la clase repositorios
            rep_id = rep.first(), 
            added_at = f"{now.year}/{now.month}/{now.day}") #Fecha de hoy
        return Response(response) 

