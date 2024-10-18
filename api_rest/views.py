from django.shortcuts import render

# importações necessárias
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

# GET para pegar todos usuários
@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



# GET para pegar por idade
@api_view(['GET'])
def get_by_idade(request, idade):

    try:
        user = User.objects.get(user_age=idade)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)


# GET para pegar por apelido
@api_view(['GET'])
def get_by_apelido(request, apelido):

    try:
        user = User.objects.get(user_nickname=apelido)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)


#CRUDZAO da massa
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request): 
    
    if request.method == 'GET':
        
        try:
            if request.GET['user']:
                
                user_nickname = request.GET['user']
                
                try:
                    user = User.objects.get(user_nickname=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)