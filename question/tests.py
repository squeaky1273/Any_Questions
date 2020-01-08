from django.test import TestCase
from django.contrib.auth.models import User

from question.models import Question

# Create your tests here.
class QuestionTestCase(TestCase):
    def test_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_question_slugify_on_save(self):
        """ Tests the slug generated when saving a Question. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # Create and save a new page to the test database.
        question = Question(title="My Test Question", description="test", author=user)
        question.save()

        # Make sure the slug that was generated in Question.save()
        # matches what we think it should be.
        self.assertEqual(playlist.slug, "my-test-question")