from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager


# Create your models here.


class CreationModificationMixin(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	last_edit_date = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Question(CreationModificationMixin):
	title = models.CharField(max_length=300)
	content = models.TextField()
	owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
							  on_delete=models.CASCADE, related_name="question_user")
	is_answered = models.BooleanField(default=True)
	score = models.BigIntegerField(default=0)

	tags = TaggableManager()

	class Meta:
		ordering = ['-creation_date']

	def __str__(self):
		return self.title[:30]

	@property
	def question_id(self):
		return self.id


class Answer(CreationModificationMixin):
	owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
							  on_delete=models.CASCADE,
							  related_name="user_answered")
	question = models.ForeignKey(to=Question,
								 on_delete=models.CASCADE,
								 related_name="answer_question")
	is_accepted = models.BooleanField(default=False)
	score = models.IntegerField(default=0)
	content = models.TextField()

# class Vote(models.Model):
#     vote = models.IntegerField(default=0)


#   {
#       
#     
#       "view_count": 484187,
#       "protected_date": 1552577593,
#       "answer_count": 36,
#  
#       "last_activity_date": 1670887275,
#     

#       "link": "https://stackoverflow.com/questions/35511604/docker-unable-to-prepare-context-unable-to-evaluate-symlinks-in-dockerfile-pa",
#
