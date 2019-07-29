from django.urls import include, path

urlpatterns = [
    path('caso/', include('caso.urls')),
    path('jogadores/', include('jogador.urls')),
    path('auth/', include('scotland.auth_urls')),

]
