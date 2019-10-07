from django.urls import path
from fib import views
from rest_framework import routers
from .views import FibViewset,UserViewSet

router = routers.DefaultRouter()
router.register(r'fib', FibViewset)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('f1/',views.demo,name='demo'),
    path('Fibform/',views.Fibform,name='Fibform'),
    path('',views.main,name='f1'),
]
