from rest_framework import viewsets, filters
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['name', 'skills']

    def get_permissions(self):
        if self.request.method == 'DELETE':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
