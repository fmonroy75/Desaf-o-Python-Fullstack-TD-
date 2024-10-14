from django.urls import path
from . import views


urlpatterns = [
    path("", views.mostrar_lista , name="lista")
    #path("app2/<str:nombre>/", views.vista_con_parametros, name="app2"),
]

