from django.urls import path
from fib import views
from rest_framework import routers
from .views import FibViewset,UserViewSet

router = routers.DefaultRouter()
router.register(r'fib', FibViewset)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('',views.demo,name='demo'),
    path('Fibform/',views.Fibform,name='Fibform'),
    path('f1/',views.f1,name='f1'),
]
