from django.urls import path
from app.views import Home
urlpatterns = [
    path('', Home, name='home')

]
