from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from api.v1.accounts.serializers import CustomUserSerializer

from api.v1.forum.models import Answer, Question


class QuestionSerializer(TaggitSerializer, serializers.ModelSerializer):
	tags = TagListSerializerField()
	# owner = CustomUserSerializer()

	class Meta:
		model = Question
		fields = (
			"id",
      		"title", 
            "content", 
            'creation_date', 
            'last_edit_date',
            'tags',
            'owner',
            
            )
		extra_kwargs = {
			"owner": {"read_only": True}
   		}
	


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = "__all__"
