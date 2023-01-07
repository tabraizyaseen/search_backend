from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import get_complete_endpoint

class searchableApps(APIView):
    "Get list of searchable apps"
    def get(self, request):
        endpoint = get_complete_endpoint(request.build_absolute_uri())
        return Response({
                    'error': False, 
                    'message':'Welcome to Zendesk Search', 
                    'data':{'Users':endpoint+'1/', 
                    'Tickets':endpoint+'2/', 
                    'Organizations':endpoint+'3/'}},
                    status=status.HTTP_200_OK)