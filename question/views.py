from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Question
from .serializers import QuestionSerializer, QuestionUploadSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('course',)

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionUploadSerializer
        return QuestionSerializer
