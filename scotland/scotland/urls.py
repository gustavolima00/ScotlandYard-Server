from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('caso/', include('caso.urls')),
    path('jogadores/', include('jogador.urls')),
    path('admin/', admin.site.urls),
    path('rest_auth/', include('scotland.auth_urls')),
]
