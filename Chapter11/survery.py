class AnonymousSurvey:
    '''Collect annonymous answers to survey questions'''
    def __init__(self, question):
        '''Store a question and prepare to store responses'''
        self.question = question
        self.responses = []
    
    def show_questions(self):
        '''Show the survey question'''
        print(self.question)
    
    def store_response(self, new_response):
        '''store a single response to the survey'''
        self.responses.append(new_response)
    
    def show_results(self):
        '''show all the responses that has been given'''
        print('Survey results: ')
        for response in self.responses:
            print(f"- {response}")

