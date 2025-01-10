from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class PingAPIView(APIView):
    """Checks if the server is ready to handle requests."""
    def get(self, request):
        return Response("ok", status=status.HTTP_200_OK)



