from django.test import TestCase
from django.urls import reverse_lazy

from rest_framework.test import APITestCase
from accounts.models import CustomUser

from forum.models import Question


# Create your tests here.

class TestCaseQuestion(APITestCase):
	url = r'http://localhost:8000/forum/questions/'

	def test_list(self):
		owner = CustomUser.objects.create(email='ed@g.com', first_name='ed', last_name='jo', password="12345678")
		question = Question.objects.create(title="Je suis un titre test1",
										   content="Je suis le content test1",
										   owner=owner,
										   is_answered=True,
										   score=2,
										   tags=["test1", "test1"])
		# Question.objects.create(title="Je suis un titre test2",
		#                                    content="Je suis le content test2",
		#                                    owner=owner,
		#                                    is_answered=False,
		#                                    score=5,
		#                                    tags=["test2", "test2" ])

		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)

		excepted = [
			{
				'id': question.id,
				'content': question.content,
				'owner': question.owner,
				'is_answered': question.is_answered,
				'score': question.score,
				'tags': question.tags,
				'creation_date': question.creation_date,
				'last_edit_date': question.last_edit_date
			}
		]
		self.assertEqual(response.json(), excepted)
