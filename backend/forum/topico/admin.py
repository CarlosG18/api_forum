from django.contrib import admin
from .models import Topico, Comentario, Postagem

# Register your models here.
admin.site.register(Topico)
admin.site.register(Comentario)
admin.site.register(Postagem)
