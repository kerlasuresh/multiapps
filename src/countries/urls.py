from django.urls import path
from countries import views

urlpatterns = [
    path('india',views.India, name='india'),
    path('chaina',views.Chaina, name='chaina'),
    path('russia',views.Russia, name='russia'),
    path('',views.homepage,name = 'countrypage')
]
