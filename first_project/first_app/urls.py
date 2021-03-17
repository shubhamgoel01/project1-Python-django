from django.urls import path
from .views import blog, contact, index


urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
]
