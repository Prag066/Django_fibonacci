from django.urls import path
from fib import views
from rest_framework import routers
from .views import FibViewset,UserViewSet

router = routers.DefaultRouter()


urlpatterns = [
    path('f1/',views.demo,name='demo'),
    path('Fibform/',views.Fibform,name='Fibform'),
    path('',views.main,name='f1'),
    path('userlist-api/',UserViewSet.as_view({'get':'list'})),
    path('fiblist-api/',FibViewset.as_view({'get':'list'})),
]
