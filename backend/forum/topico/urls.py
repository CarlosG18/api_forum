from django.urls import path
from . import views

urlpatterns = [
    path('create_topico/', views.create_topico),
    path('all/', views.all_topics),
    path('<int:id>/', views.topic_detal),
    path('create_postagem/', views.create_postagem),
    path('all_postagens/', views.all_postagem),
    path('all_comentarios/', views.all_comentario),
    path('create_comentario/', views.create_comentario),
    path('votar/', views.update_votacao),
]