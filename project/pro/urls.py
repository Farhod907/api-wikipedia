from django.urls import path
from .views import Wikipedia
urlpatterns = [
    # path('',Was, name="first"),
    path('api/',Wikipedia, name='wikipedia'),
]