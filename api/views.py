from django.shortcuts import render
from .models import Client
from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def toList_Clients(request):
    if request.method == 'GET':
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientsView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
