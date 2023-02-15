from django.urls import path
from courses import views

urlpatterns = [
    path('python',views.python, name='py'),
    path('django',views.django, name='dj'),
    path('js',views.javascript, name='js'),
    path('',views.homepage,name='coursespage')

]
