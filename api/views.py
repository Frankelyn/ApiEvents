from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Evento, Seccion
from .serializers import EventoSerializer, SeccionSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer


# Métodos para la clase Evento

@api_view(['GET'])
def get_eventos(request):
    eventos = Evento.objects.all()
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_evento(request, id_evento):
    evento = Evento.objects.get(id_evento=id_evento)
    serializer = EventoSerializer(evento)
    return Response(serializer.data)

@api_view(['POST'])
def create_evento(request):
    serializer = EventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_evento(request, id_evento):
    evento = Evento.objects.get(id_evento=id_evento)
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_evento(request, id_evento):
    evento = Evento.objects.get(id_evento=id_evento)
    evento.delete()
    return Response(status=204)

# Métodos para la clase Seccion

@api_view(['GET'])
def get_secciones(request):
    secciones = Seccion.objects.all()
    serializer = SeccionSerializer(secciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_seccion(request, id_seccion):
    seccion = Seccion.objects.get(id_seccion=id_seccion)
    serializer = SeccionSerializer(seccion)
    return Response(serializer.data)

@api_view(['POST'])
def create_seccion(request):
    serializer = SeccionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_seccion(request, id_seccion):
    seccion = Seccion.objects.get(id_seccion=id_seccion)
    serializer = SeccionSerializer(seccion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_seccion(request, id_seccion):
    seccion = Seccion.objects.get(id_seccion=id_seccion)
    seccion.delete()
    return Response(status=204)

