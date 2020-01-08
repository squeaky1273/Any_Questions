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