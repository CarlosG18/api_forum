from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topico, Postagem, Comentario
from django.contrib.auth.models import User
from .serializers import TopicoSerializer, PostagemSerializer, ComentarioSerializer
from rest_framework import status

#endpoint para criação de um topico
@api_view(['POST'])
def create_topico(request):
    data = request.data
    serial_data = TopicoSerializer(data=data)
    if serial_data.is_valid():
        response = {
            "status": "sucess",
            "messagem": "topico criado com sucesso",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        serial_data.save()
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint para obter todos os topicos
@api_view(['GET'])
def all_topics(request):
    queryset = Topico.objects.all()
    queryset_serial = TopicoSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos os topicos obtidos com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

#endpoint para retornar detalhes de um topico atraves do id
@api_view(['GET'])
def topic_detal(request, id):
    topico = Topico.objects.get(id=id)
    topico_serial = TopicoSerializer(topico)
    response = {
            "status": "sucess",
            "messagem": "topico obtido com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": topico_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

#endpoint para obter todas as postagens
@api_view(['GET'])
def all_postagem(request):
    postagens = Postagem.objects.all()
    postagens_serial = PostagemSerializer(postagens, many=True)
    response = {
            "status": "sucess",
            "messagem": "postagens obtidas com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": postagens_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

#endpoint para criação de um postagem
@api_view(['POST'])
def create_postagem(request):
    data = request.data
    serial_data = PostagemSerializer(data=data)
    
    if serial_data.is_valid():
        serial_data.save()
        response = {
            "status": "sucess",
            "messagem": "postagem criada com sucesso",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint para obter todas as postagens
@api_view(['GET'])
def all_comentario(request):
    comentarios = Comentario.objects.all()
    comentarios_serial = ComentarioSerializer(comentarios, many=True)
    response = {
            "status": "sucess",
            "messagem": "comentarios obtidas com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": comentarios_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

#endpoint para criação de um comentario
@api_view(['POST'])
def create_comentario(request):
    data = request.data
    serial_data = ComentarioSerializer(data=data)
    
    if serial_data.is_valid():
        serial_data.save()
        response = {
            "status": "sucess",
            "messagem": "comentario criado com sucesso",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)

#endpoint para editar os votos de positivo ou negativo
@api_view(['PUT'])
def update_votacao(request):
    try:
        id_comentario = request.data["id_comentario"]
        tipo = request.data["tipo"]
    except KeyError as e:
        return Response(f'campo vazio {e}', status=status.HTTP_400_BAD_REQUEST)
    else:
        comentario = Comentario.objects.get(id=id_comentario)
        comentario.update_voto(tipo)
        comentario.save()
        comentario_serial = ComentarioSerializer(comentario)
        response = {
                "status": "sucess",
                "messagem": "voto realizado com sucesso!",
                "code": status.HTTP_200_OK,
                "dados": comentario_serial.data
            }
        return Response(response, status=status.HTTP_200_OK)    