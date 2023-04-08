from django.urls import path
from my_app.views import hello_world

urlpatterns = [
    path('hello', hello_world),
]