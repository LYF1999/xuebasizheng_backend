from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Question
from utils.response import Response
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

    def create(self, request, *args, **kwargs):
        questions_serializer: QuestionSerializer = self.get_serializer(data=request.data)
        questions_serializer.is_valid(raise_exception=True)
        questions = questions_serializer.save()
        return Response.ok(QuestionSerializer(questions).data)
