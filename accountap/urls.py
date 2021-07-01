from django.urls import path

from accountap.views import hello_world

app_name = "accountap"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]