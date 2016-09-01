import datetime

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
    def get(request, init_date=None, end_date=None, user_id=None,
            user_email=None):
        status_code = status.HTTP_204_NO_CONTENT
        data = {}
        filter_data = {}
        error = False
        init_date = init_date or request.query_params.get('init_date')
        end_date = end_date or request.query_params.get('end_date')
        if init_date and end_date:
            try:
                init_date = datetime.datetime.strptime(init_date, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                status_code = status.HTTP_400_BAD_REQUEST
                error = True
            else:
                end_date = end_date + datetime.timedelta(days=1)
                filter_data['when__range'] = (init_date, end_date)

        user_id = user_id or request.query_params.get('user_id')
        if user_id:
            filter_data['user__id'] = user_id

        user_email = user_email or request.query_params.get('user_email')
        if user_email:
            filter_data['user__email'] = user_email

        mandadas = Mandada.objects.filter(**filter_data)
        if mandadas.exists() and not error:
            serializer = MandadaSerializer(mandadas, many=True)
            status_code = status.HTTP_200_OK
            data = serializer.data
        return Response(data, status=status_code)
