from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('visiteur/<str:id_visiteur>/', views.visiteur_detail, name='visiteur_detail'),
    path('visiteur/<str:id_visiteur>/?<str:message>', views.visiteur_detail, name='visiteur_detail_mes'),

]