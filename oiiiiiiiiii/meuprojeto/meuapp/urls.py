from django.url import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
]