from rest_framework import serializers
from .models import Topico, Comentario, Postagem
from django.contrib.auth.models import User
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

class TopicoSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    assunto = serializers.CharField()
    data_criacao = serializers.DateTimeField()
    titulo = serializers.CharField()

    def create(self, data):
        return Topico.objects.create(**data)

    def update(self, instance, data):
        instance.user = data.get('user', instance.user)
        instance.assunto = data.get('assunto', instance.assunto)
        instance.data_criacao = data.get('data_criacao', instance.data_criacao)
        instance.titulo = data.get('titulo', instance.titulo)
        instance.save()
        return instance

class ComentarioSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    conteudo = serializers.CharField()
    data_criacao = serializers.DateTimeField()
    postagem = serializers.PrimaryKeyRelatedField(queryset=Postagem.objects.all())
    votos_positivos = serializers.IntegerField()
    votos_negativos = serializers.IntegerField()

    def validate(self, data):
        if data['votos_positivos'] < 0 or data['votos_negativos'] < 0:
            raise serializers.ValidationError("não é posivel ter votos negativos!")

        return data

    def create(self, data):
        return Comentario.objects.create(**data)
    
    def update(self, instance, data):
        instance.user = data.get('user', instance.user)
        instance.conteudo = data.get('conteudo', instance.conteudo)
        instance.data_criacao = data.get('data_criacao', instance.data_criacao)
        instance.postagem = data.get('postagem', instance.postagem)
        instance.votos_positivos = data.get('votos_positivos', instance.votos_positivos)
        instance.votos_negativos = data.get('votos_negativos', instance.votos_negativos)
        instance.save()
        return instance
        

class PostagemSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    topico = serializers.PrimaryKeyRelatedField(queryset=Topico.objects.all())
    conteudo = serializers.CharField()

    def create(self, data):
        return Postagem.objects.create(**data)

    def update(self, instance, data):
        instance.user = data.get('user', instance.user)
        instance.topico = data.get('topico', instance.topico)
        instance.conteudo = data.get('conteudo', instance.conteudo)