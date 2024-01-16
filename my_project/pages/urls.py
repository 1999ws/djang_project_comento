from django.urls import path
from . import views
urlpatterns = [
    path('',views.main),
    path('main/',views.main),
    path('opinion/',views.opinion),
    path('opinion_1/',views.opinion_1),
    path('opinion_1_article1/',views.opinion_1_article1),
    path('opinion_2/',views.opinion_2),
    path('politics/',views.policits),
    path('public/',views.public),
    path('economy/',views.economy),
    path('sports/',views.sports),
    path('entertainment/',views.entertainment),
]   
