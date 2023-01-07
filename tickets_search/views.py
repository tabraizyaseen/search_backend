from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from search_backend.secrets import tickets_search_col
from search_backend.utils import get_mongo_connection, get_complete_endpoint, string2bool

# Create your views here.
class ticketSearchableFields(APIView):
    "Get list of searchable values"

    def get(self, request):
        endpoint = get_complete_endpoint(request.build_absolute_uri())
        col_conn = get_mongo_connection(tickets_search_col)
        result = col_conn.find_one()
        data = {k:endpoint+k+'?value=<insert_your_value_here>' for k in result.keys()}
        return Response({
                'error': False, 
                'message':'List of Searchable Values', 
                'data': data },
                status=status.HTTP_200_OK)

class ticketSearchValue(APIView):
    "Get list of searchable values"

    def get(self, request, value_name):
        endpoint = get_complete_endpoint(request.build_absolute_uri())
        col_conn = get_mongo_connection(tickets_search_col)
        result = col_conn.find_one()
        if value_name in result.keys():
            if 'value' in request.query_params.keys():
                search_value = request.query_params['value']

                # Handling search of integer values
                if search_value.isdigit():
                    search_value = int(search_value)
                
                # To handle boolean fields search
                if value_name in ['has_incidents']:
                    search_value = string2bool(search_value)
                
                results = list(col_conn.find({value_name:search_value}))
                return Response({
                        'error': False, 
                        'message':'Search Results', 
                        'data': results },
                        status=status.HTTP_200_OK)
                    
            # If value query parameter isn't given
            endpoint = endpoint + '?value=<insert_your_value_here>'
            return Response({
                    'error': True, 
                    'message':'Please Provide Value Query Parameter', 
                    'data': {value_name:endpoint} },
                    status=status.HTTP_400_BAD_REQUEST)
        
        # If value_name isn't correct
        endpoint = endpoint.replace(value_name+'/','')
        data = {k:endpoint+k+'?value=<insert_your_value_here>' for k in result.keys()}
        return Response({
                    'error': True, 
                    'message':'Please Search on These Values', 
                    'data': data },
                    status=status.HTTP_400_BAD_REQUEST)
        