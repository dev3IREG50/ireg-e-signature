"""
Module: views.py

- This module defines a Django REST Framework view for listing signing
  documents.

View:
- `SigningDocumentListAPIView`: View for listing signing documents.

"""


from rest_framework import generics
from ..models import Signing
from ..serializers import  (
    SigningSerializer,
)

from base.api.permissions.document_permission import IsOwnerOrReadOnly


class SigningDocumentListAPIView(generics.ListAPIView):
    """
        View for listing signing documents.

        Attributes:
        - queryset: Queryset containing all Signing objects.
        - serializer_class: Serializer class for serializing Signing
          objects.
        - permission_classes: List of permission classes, including
          IsOwnerOrReadOnly.

        Methods:
        - get_queryset(): Custom method to filter the queryset based on
          the requesting user.
    """
    queryset = Signing.objects.all()
    serializer_class = SigningSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filter queryset based on the user making the request
        return self.queryset.filter(document__owner=self.request.user)