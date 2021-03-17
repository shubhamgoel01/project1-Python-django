from django.urls import path
from .views import blog, contact, index


urlpatterns = [
    path('', index, name='Home'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
]
