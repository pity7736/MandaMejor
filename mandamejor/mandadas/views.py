import datetime

from django.http.response import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .controllers.mandadas_controller import MandadaController
from .serializers import MandadaSerializer


def index(request):
    return HttpResponse('hello')


class MandadasView(APIView):

    @staticmethod
    def get(request, init_date=None, end_date=None, user_id=None,
            user_email=None):
        status_code = status.HTTP_204_NO_CONTENT
        data = {}
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
                init_date = None
                end_date = None
            else:
                end_date = end_date + datetime.timedelta(days=1)

        user_id = user_id or request.query_params.get('user_id')
        user_email = user_email or request.query_params.get('user_email')

        mandadas_controller = MandadaController(
            init_date=init_date,
            end_date=end_date,
            user_email=user_email,
            user_id=user_id
        )
        mandadas = mandadas_controller.run_query()
        if mandadas.exists() and not error:
            serializer = MandadaSerializer(mandadas, many=True)
            status_code = status.HTTP_200_OK
            data['data'] = serializer.data

        data['count'] = mandadas.count()
        return Response(data, status=status_code)
