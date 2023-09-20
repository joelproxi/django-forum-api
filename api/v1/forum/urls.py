from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.v1.forum import views



router = DefaultRouter()
router.register("questions", views.QuestionViewset, basename="questions")

forum_answer_router = routers.NestedDefaultRouter(router, r'questions', lookup='questions')

forum_answer_router.register("answers", views.AnswerViewset, basename='question-answers'),