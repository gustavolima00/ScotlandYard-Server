from django.urls import include, path

urlpatterns = [
    path('caso/', include('caso.urls')),
    path('jogador/', include('jogador.urls')),
    path('sala/', include('sala.urls')),
    path('auth/', include('scotland.auth_urls')),

]
