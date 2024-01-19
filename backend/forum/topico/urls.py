from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_topico),
    path('all/', views.all_topics)
]