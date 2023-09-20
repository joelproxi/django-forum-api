from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from api.v1.forum.models import Answer, Question
from api.v1.forum.serializers import AnswerSerializer, QuestionSerializer
from api.v1.forum.paginations import ForumPagination
from core import permissions
# Create your views here.

class QuestionViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthorStaffEditOrReadonly, ]
    queryset = Question.objects\
        .select_related("owner")\
        .prefetch_related('tags')
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content', 'tags__name']
    search_fields = ['title', 'content', 'tags__name']
    # pagination_class = ForumPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return serializer
    

class AnswerViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthorStaffEditOrReadonly]
    queryset = Answer.objects.\
        select_related("owner", "question")
    serializer_class = AnswerSerializer
    
    def get_queryset(self):
        question_id = self.kwargs.get("questions_pk")
        question = get_object_or_404(Question, pk=question_id)
        answer_list = Answer.objects.select_related("owner", "question")\
            .filter(question__id=question.id)
        return answer_list
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return serializer
    
    