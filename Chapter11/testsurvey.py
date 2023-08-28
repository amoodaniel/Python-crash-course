import unittest
from survery import AnonymousSurvey

class SurveyTestCase(unittest.TestCase):
    def test_single_response(self):
        question = 'What language did you learn first'
        survey = AnonymousSurvey(question)
        correct_value = survey.store_response('English')
        self.assertIn('English', survey.responses)
    def test_three_response(self):
        question = 'What language did you learn first'
        survey = AnonymousSurvey(question)
        responses = ['English', 'Mandarin', 'Arabic']
        for response in responses:
            survey.store_response(response)
        for response in responses:
            self.assertIn(response, survey.responses)

if __name__ == '__main__':
    unittest.main()