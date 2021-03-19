from django.urls import path
from .views import blog, contact, index, showAllContacts


urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('showAllContacts', showAllContacts, name="showAllContacts")
]
