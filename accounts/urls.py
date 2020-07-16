from django.urls import path, include
urlpatterns = [
    path('api/',include('djoser.urls')),
    path('api/',include('djoser.urls.jwt'))
]
