from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """
    Test API view
    """
    def get(self, request, format=None):
        """
        Returns a list of API view features
        """
        an_apiview = [
            'Uses HTTP methods as functions (GET, POST, PATCH, PUT, DELETE)',
            'Similar to a traditional Django view, but specifically for APIs',
            'Gives you the most control over your application logic',
            'Manually mapped to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
