from django.urls import include, path

app_name = 'api_v1'

urlpatterns = [
    path('youtube/', include('server.youtube.urls')),
]
