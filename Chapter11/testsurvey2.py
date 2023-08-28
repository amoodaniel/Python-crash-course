import unittest
from survery import AnonymousSurvey

class SurveyTestCase(unittest.TestCase):
    def setUp(self):
        '''Create a survey and a set of responses for use in all test methods'''
        question = 'What language did you learn first'
        self.mysurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Spanish']

    def test_single_response(self):
        self.mysurvey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.mysurvey.responses)
    def test_three_response(self):
        for response in self.responses:
            self.mysurvey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.mysurvey.responses)

if __name__ == '__main__':
    unittest.main()