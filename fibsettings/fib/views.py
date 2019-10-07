from django.shortcuts import render
import time
from datetime import datetime
from .forms import Fib_data_Form
from .models import Fib_data
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import FibSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

def main(request):
    arr = []
    if request.method == "POST":
        stime = datetime.now()
        n = request.POST['val1']
        if n == '':
            n = 0

        a,b = 1,1
        arr = [a,b]
        for i in range(1,int(n)):
            c = a + b
            r = arr.append(c)
            a = b
            b = c
        etime = datetime.now()
        tdelta = etime - stime
        m = Fib_data()
        m.number = n
        m.duretion = tdelta
        m.fib_list = arr
        m.save()
    else:
        n = ''
        tdelta = None
    return render(request,'f1.html',{'num':arr,'tdelta':tdelta})

def Fibform(request):
    if request.method == "POST":
        form = Fib_data_Form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Fib_data_Form()
    return render(request,'f.html',{'form':form})

def demo(request):
    timeinst1 = time.localtime()
    stime = datetime.now()
    arr = []
    if request.method == "POST":
        num = request.POST['num']

        if num is not '':
            num = int(num)
        else:
            num = int()

        a = 1
        b = 1
        arr = [1,1]

        for i in range(1,num):
            c = a + b
            r = arr.append(c)
            a = b
            b = c
    time.sleep(1)
    timeinst2 = time.localtime()
    etime = datetime.now()

    tdelta = etime -stime

    return render(request, 'h.html', {'tdelta':[tdelta.seconds,tdelta.microseconds],'context': arr})

@permission_classes((permissions.AllowAny,))
class FibViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Fib_data.objects.all()
        serializer = FibSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Fib_data.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FibSerializer(user)
        return Response(serializer.data)
    
    queryset = User.objects.all()
    serializer_class = FibSerializer



@permission_classes((permissions.AllowAny,))
class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
