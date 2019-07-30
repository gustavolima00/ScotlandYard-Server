from django.urls import include, path

urlpatterns = [
    path('case/', include('caso.urls')),
    path('player/', include('jogador.urls')),
    path('room/', include('sala.urls')),
    path('auth/', include('scotland.auth_urls')),

]
