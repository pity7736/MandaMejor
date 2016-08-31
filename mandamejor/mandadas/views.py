from django.http.response import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mandada
from .serializers import MandadaSerializer


def index(request):
    return HttpResponse('hello')


class MandadasView(APIView):

    @staticmethod
    def get(request):
        status_code = status.HTTP_204_NO_CONTENT
        data = []
        mandadas = Mandada.objects.all()
        if mandadas.exists():
            serializer = MandadaSerializer(mandadas, many=True)
            status_code = status.HTTP_200_OK
            data = serializer.data
        return Response(data, status=status_code)


class MandadasByUserView(APIView):

    @staticmethod
    def get(request, user_id):
        status_code = status.HTTP_204_NO_CONTENT
        mandadas = Mandada.objects.filter(user__id=user_id)
        data = []
        if mandadas.exists():
            serializer = MandadaSerializer(mandadas, many=True)
            status_code = status.HTTP_200_OK
            data = serializer.data
        return Response(data, status=status_code)
