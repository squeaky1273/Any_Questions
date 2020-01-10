from django.test import TestCase
from django.contrib.auth.models import User

from question.models import Question

# Create your tests here.
class QuestionTestCase(TestCase):
    def test_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_question_slugify_on_save(self):
        """ Tests that the slug is generated when saving a Question. """
        # Author is a required field in our model.
        # Create a user and save it to the test database.
        user = User()
        user.save()

        # Create and save a new question to the test database.
        question = Question(question_text="Will This Work?", author=user)
        question.save()

        # Make sure the generated slug in Question.save() above
        # matches what we think it should show up.
        self.assertEqual(question.slug, "will-this-work")

class QuestionCreateFormTests(TestCase):
    def test_load_details(self):
        response = self.client.get('/new_question/')
        self.assertEqual(response.status_code, 200)
"""
    def test_new_question(self):
        user = User.objects.create()

        data = {
            'question_test': 'What is a detail question?',
            'author': user,
        }

        response = self.client.post(reverse_lazy('question-details-page', args=['detail-page'])), data=data, follow=True)
        self.assertEqual(response.status_code, 302)
"""
"""
class QuestionListViewTests(TestCase):
    def test_multiple_questions(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Question.objects.create(title="What is a test question?", content="test", author=user)
        Question.objects.create(title="Is there another test question?", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['questions']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Question: What is a test question?>', '<Question: Is there a another test question?>'],
            ordered=False
        )
"""
"""
class QuestionDetailViewTests(TestCase) :
    def test_load_specific_question(self):
        user = User.objects.create()

        question = Question.objects.create(title="What is a detail question?", author=user)

        slug = question.slug

        response = self.client.get(f'/{slug}/')

        self.assertEqual(response.status_code, 200)
"""