# from django.test import TestCase, Client
# from django.contrib.auth.models import User
# from .models import Question, Answer, Liked


# class LikedTest(TestCase):

#     def setUp(self):
#         self.user1 = User.objects.create(username='user_1')
#         self.user2 = User.objects.create(username='user_2')

#         question = Question.objects.create(question='What is the meaning of life?', author=self.user1)
#         self.answer1 = Answer.objects.create(ans='42', question=question, author=self.user1)
#         self.answer2 = Answer.objects.create(ans='The universe', question=question, author=self.user2)

#         self.client1 = Client()
#         self.client1.force_login(self.user1)

#         self.client2 = Client()
#         self.client2.force_login(self.user2)

#     def test_like_answer(self):
#         # User 1 likes the answer from user2.
#         response = self.client1.post(f'/answer/like/{self.answer2.id}/')
#         self.assertEqual(response.status_code, 302)

#         # Check that user 1 has liked the answer from user2.
#         liked_answers = Liked.objects.filter(user=self.user1)
#         self.assertEqual(len(liked_answers), 1)
#         self.assertEqual(liked_answers[0].answer, self.answer2)

#         # Check that user 2 has not liked the answer from user1.
#         liked_answers = Liked.objects.filter(user=self.user2)
#         self.assertEqual(len(liked_answers), 0)

#         # User 2 likes the answer from user1.
#         response = self.client2.post(f'/answer/like/{self.answer1.id}/')
#         self.assertEqual(response.status_code, 302)

#         # Check that user 2 has liked the answer from user1.
#         liked_answers = Liked.objects.filter(user=self.user2)
#         self.assertEqual(len(liked_answers), 1)
#         self.assertEqual(liked_answers[0].answer, self.answer1)

#         # Check that user 1 has also liked the answer from user2.
#         liked_answers = Liked.objects.filter(user=self.user1)
#         self.assertEqual(len(liked_answers), 1)
