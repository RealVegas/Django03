from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='lorem'),
    path('Что_такое_Lorem_ipsum', views.info, name='info'),
    path('Английские_панграммы', views.pan_eng, name='pan_eng'),
    path('Русские_панграммы', views.pan_rus, name='pan_rus')
]