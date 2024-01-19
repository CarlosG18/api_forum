from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    tipos_de_assunto = [
        "Tecnologia e Inovação",
        "Ciência e Descobertas",
        "Saúde e Bem-estar",
        "Educação e Aprendizado",
        "Meio Ambiente e Sustentabilidade",
        "Arte e Cultura",
        "Viagens e Aventuras",
        "Filmes, Séries e Entretenimento",
        "Esportes e Atividades Físicas",
        "Negócios e Empreendedorismo",
        "Finanças Pessoais e Investimentos",
        "Relacionamentos e Vida Social",
        "Política e Atualidades",
        "Moda e Estilo",
        "Culinária e Gastronomia",
        "Hobbies e Passatempos",
        "Dicas de Livros e Leitura",
        "Automóveis e Tecnologia Automotiva",
        "Parentalidade e Família",
        "Fotografia e Arte Visual",
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200, choices=[(assunto,assunto) for assunto in tipos_de_assunto])
    data_criacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return f'topico: {self.titulo}'
    

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    topico = models.ManyToManyField(Topico)
    votos_positivos = models.IntegerField(default=0)
    votos_negativos = models.IntegerField(default=0)

    def __str__(self):
        topicos_str = ', '.join([str(topico) for topico in self.topico.all()])
        return f'comentario do {self.user.username} sobre o {topicos_str}'