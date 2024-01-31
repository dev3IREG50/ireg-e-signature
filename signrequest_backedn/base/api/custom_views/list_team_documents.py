"""
Module: team_document_views

- This module contains views related to team documents in a Django
  REST framework API.

Classes:
    - ListTeamDocumentsView: A view class that retrieves and serializes
                             TeamDocumentSigning instances associated with
                             a specific team.
    - ListAllTeamDocumentsView: A view class that retrieves and serializes
                                all TeamDocumentSigning instances
                                without being specific to a single team.

Note: This module assumes the existence of the following:
    - Models: TeamDocumentSigning
    - Serializers: TeamSigningSerializer
"""

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import TeamDocumentSigning
from ..serializers import TeamSigningSerializer

class ListTeamDocumentsView(ListAPIView):
    """
    - View class for listing TeamDocumentSigning instances related to a
      specific team.

    Attributes:
        - serializer_class (class): The serializer class to use for
          serializing the data.
        - permission_classes (list): The list of permission classes
          required for accessing the view.

    Methods:
        - get_queryset(): Returns a queryset of TeamDocumentSigning instances
          filtered by team_id.
        - list(request, *args, **kwargs): Retrieves and serializes the queryset,
          then returns the response.
    """
    serializer_class = TeamSigningSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns a queryset of TeamDocumentSigning instances filtered by team_id.

        Returns:
            queryset: A filtered queryset of TeamDocumentSigning instances.
        """
        # Filter documents based on the team_id parameter
        team_id = self.kwargs.get('team_id')
        # Here, we are filtering TeamDocumentSigning instances based on the related Team
        # through the document foreign key. The __team_id part is referencing the
        # team field in the TeamDocument model.
        return TeamDocumentSigning.objects.filter(document__team_id=team_id)
    
    def list(self, request, *args, **kwargs):
        """
        Retrieves and serializes the queryset, then returns the response.

        Args:
            request: The HTTP request object.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            Response: The serialized data wrapped in a Response object.
        """
        queryset = self.get_queryset()

        # Serialize the team documents data
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class ListAllTeamDocumentsView(ListAPIView):
    """
    View class for listing all TeamDocumentSigning instances.

    Attributes:
        - queryset (queryset): The queryset of all TeamDocumentSigning
          instances.
        - serializer_class (class): The serializer class to use for
          serializing the data.
        - permission_classes (list): The list of permission classes
          required for accessing the view.
    """
    queryset = TeamDocumentSigning.objects.all()
    serializer_class = TeamSigningSerializer
    permission_classes = [IsAuthenticated]

