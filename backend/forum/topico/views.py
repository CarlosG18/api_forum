from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topico
from django.contrib.auth.models import User
from .serializers import TopicoSerializer

#endpoint para criação de um topico
@api_view(['POST'])
def create_topico(request):
    data = request.data
    serial_data = TopicoSerializer(data=data)
    if serial_data.is_valid():
        serial_data.save()
        return Response("deu certo!")
    else:
        return Response(serial_data.errors)

@api_view(['GET'])
def all_topics(request):
    queryset = Topico.objects.all()
    queryset_serial = TopicoSerializer(queryset, many=True)
    return Response(queryset_serial.data)

#endpoint para criação de um postagem
@api_view(['POST'])
def create_postagem(request):
    pass

#endpoint para criação de um comentario
@api_view(['POST'])
def create_comentario(request):
    pass

#endpoint para editar os votos de positivo ou negativo
@api_view(['POST'])
def update_votacao(request):
    pass